from readme_generator.agents.readme_state import ReadmeState, Review
from readme_generator.helpers.chat_ollama import chat_ollama


def review(state: ReadmeState):
    print("Reviewing...")

    prompt = f"""You are a strict reviewer of README files.

    Technical analysis of the repository:
    {state["analysis"]}

    README draft:
    {state["readme_draft"]}

    Give a score from 0 to 10 and your feedback based on:
    - Accuracy: everything matches the analysis, nothing invented
    - Completeness: a new developer can install and run the project
    - Clarity: easy to read, good structure
    - Formatting: correct Markdown, commands in code blocks

    A score of 7 or more means it is ready to publish.
    In the feedback, list only concrete things to fix. If the score is 8 or more, the feedback can be short."""

    response = chat_ollama.with_structured_output(Review).invoke(prompt)
    return {
        "reviews": [response]
    }
