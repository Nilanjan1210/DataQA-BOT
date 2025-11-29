# agents/base.py
from abc import ABC, abstractmethod
from langchain_core.messages import HumanMessage
from typing import Any

class BaseAgent(ABC):
    def __init__(self, llm, name: str):
        self.llm = llm
        self.name = name

    @abstractmethod
    def run(self, input_text: str) -> str:
        pass