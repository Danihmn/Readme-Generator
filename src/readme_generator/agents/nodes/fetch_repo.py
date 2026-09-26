from readme_generator.agents.readme_state import ReadmeState, RepoFile
from readme_generator.helpers.fetch_github_repo import fetch_github_repo


def fetch_repo(state: ReadmeState):
    print()
    print("Fetching repo...")

    repo: dict = fetch_github_repo(state["repo_url"])
    return {
        "repo_name": repo["repo_name"],
        "files": [RepoFile(path=file["path"], content=file["content"]) for file in repo["files"]],
    }
