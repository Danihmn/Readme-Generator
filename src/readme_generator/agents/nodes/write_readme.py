from readme_generator.agents.readme_state import ReadmeState
from readme_generator.helpers.chat_ollama import chat_ollama


def write_readme(state: ReadmeState):
    print("Writing readme...")

    prompt = f"""You are a technical writer. Write a README.md for this repository.

    Repository: {state["repo_name"]}

    Technical analysis:
    {state["analysis"]}

    {[review for review in state["reviews"].feedback] if state["reviews"] else ""}

    Rules:
    - Use Markdown
    - Sections: title, short description, features, tech stack, getting started (prerequisites, installation, running), environment variables (only if any), project structure
    - Keep it clear and direct, no marketing language
    - Commands must be in code blocks
    - Do not invent features, commands or links that are not in the analysis

    Return only the README content, without any extra text."""

    response = chat_ollama.invoke(prompt)
    return {
        "readme_draft": response.content if response else ""
    }
