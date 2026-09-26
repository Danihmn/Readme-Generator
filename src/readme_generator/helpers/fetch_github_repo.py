import os

from urllib.parse import urlparse
from github import Github, Auth

ALLOWED_EXTENSIONS = {".py", ".cs", ".dart", ".js", ".ts", ".json", ".toml", ".yaml", ".yml", ".md"}
MAX_FILES = 30
MAX_FILE_SIZE = 20_000  # bytes


def parse_repo_url(url: str) -> str:
    """'https://github.com/owner/repo' -> 'owner/repo'"""
    path = urlparse(url).path.strip("/").removesuffix(".git")
    owner, repo = path.split("/")[:2]
    return f"{owner}/{repo}"


def fetch_github_repo(repo_url: str) -> dict:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN not found. Check your .env file.")

    github = Github(auth=Auth.Token(token))

    try:
        repo = github.get_repo(parse_repo_url(repo_url))
        tree = repo.get_git_tree(repo.default_branch, recursive=True)

        files = []

        for item in tree.tree:
            if item.type != "blob":
                continue
            if not any(item.path.endswith(extension) for extension in ALLOWED_EXTENSIONS):
                continue
            if item.size and item.size > MAX_FILE_SIZE:
                continue

            content = repo.get_contents(item.path, ref=repo.default_branch)
            files.append({
                "path": item.path,
                "content": content.decoded_content.decode("utf-8", errors="ignore"),
            })

            if len(files) >= MAX_FILES:
                break

        return {"repo_name": repo.full_name, "files": files}
    finally:
        github.close()
