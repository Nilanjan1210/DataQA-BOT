from typing import Sequence, TypedDict, Annotated
from typing_extensions import NotRequired


from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class State(TypedDict):
    """TypedDict for the entire state structure."""
    # The sequence of messages exchanged in the conversation
    messages: Annotated[Sequence[BaseMessage], add_messages]
