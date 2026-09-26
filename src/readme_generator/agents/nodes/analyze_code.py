from readme_generator.agents.readme_state import ReadmeState
from readme_generator.helpers.chat_ollama import chat_ollama


def analyze_code(state: ReadmeState):
    print("Analyzing code...")

    prompt = f"""You are a senior software engineer reviewing a GitHub repository.

    Repository: {state["repo_name"]}

    Files:
    {state["files"]}

    Analyze the code and write a short technical summary with:
    - Purpose: what the project does, in 1-2 sentences
    - Stack: languages, frameworks and main libraries
    - Structure: main folders and what each one contains
    - How to run: install and run commands, based on config files (package.json, requirements.txt, pyproject.toml, .csproj, pubspec.yaml, etc.)
    - Environment variables: any env vars the code reads

    Only describe what you can see in the files. If something is not clear, write "not found" instead of guessing."""

    response = chat_ollama.invoke(prompt)
    return {"analysis": response.content if response else "not found"}
