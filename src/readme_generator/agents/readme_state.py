import operator
from typing import TypedDict, Annotated, Literal

from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages


class RepoFile(TypedDict):
    path: str
    content: str


class Review(TypedDict):
    score: int
    feedback: str


class ReadmeState(TypedDict):
    repo_url: str
    repo_name: str
    files: list[RepoFile]
    analysis: str
    readme_draft: str
    reviews: Annotated[list[Review], operator.add]
    attempts: int
    messages: Annotated[list[BaseMessage], add_messages]
    human_decision: Literal["approved", "changes_requested"] | None
    human_feedback: str | None
