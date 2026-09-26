from readme_generator.agents.graph import readme_generator_agent
from readme_generator.agents.readme_state import ReadmeState

repo_url = input("Enter repo url: ")
initial_state: ReadmeState = {
    "repo_url": repo_url,
    "repo_name": "",
    "files": [],
    "analysis": "",
    "readme_draft": "",
    "reviews": [],
    "attempts": 0,
    "human_decision": None,
    "human_feedback": None,
}

response = readme_generator_agent.invoke(initial_state)
