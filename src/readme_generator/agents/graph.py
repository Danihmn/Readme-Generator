from typing import Literal

from langgraph.constants import START
from langgraph.graph import StateGraph

from readme_generator.agents.nodes import fetch_repo, analyze_code, write_readme, review, human_approval
from readme_generator.agents.readme_state import ReadmeState

builder = StateGraph(ReadmeState)

builder.add_node("fetch_repo", fetch_repo)
builder.add_node("analyze_code", analyze_code)
builder.add_node("write_readme", write_readme)
builder.add_node("review", review)
builder.add_node("human_approval", human_approval)


def _should_rewrite_readme_decided_by_llm(state: ReadmeState) -> Literal["analyze_code", "human_approval"]:
    """The LLM reviews the generated README.md and decide if it's great or not"""
    reviews = state["reviews"]
    if reviews[-1]["score"] < 7:
        return "analyze_code"
    return "human_approval"


builder.add_edge(START, "fetch_repo")
builder.add_edge("fetch_repo", "analyze_code")
builder.add_edge("analyze_code", "write_readme")
builder.add_edge("write_readme", "review")
builder.add_conditional_edges(
    "review",
    _should_rewrite_readme_decided_by_llm,
    ["analyze_code", "human_approval"])

readme_generator_agent = builder.compile()
