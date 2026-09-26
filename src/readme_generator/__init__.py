import json

from load_dotenv import load_dotenv
from langchain_core.messages import messages_to_dict

from readme_generator.agents.graph import readme_generator_agent
from readme_generator.agents.readme_state import ReadmeState

load_dotenv()

repo_url = input("Enter repo url: ")
initial_state: ReadmeState = {
    "repo_url": repo_url,
    "repo_name": "",
    "files": [],
    "analysis": "",
    "readme_draft": "",
    "reviews": [],
    "attempts": 0,
    "messages": [],
    "human_decision": None,
    "human_feedback": None,
}

response = readme_generator_agent.invoke(initial_state)

output = {**response, "messages": messages_to_dict(response["messages"])}
print(json.dumps(output, indent=4, ensure_ascii=False))
