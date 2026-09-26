import operator
from typing import TypedDict, Annotated, Literal


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
    human_decision: Literal["approved", "changes_requested"] | None
    human_feedback: str | None
