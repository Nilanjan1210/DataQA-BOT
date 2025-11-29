from typing import Type
import os
from langchain_groq import ChatGroq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def llm(model = "openai/gpt-oss-120b", api_key = GROQ_API_KEY, temperature = 0):
    return ChatGroq(
        model=model,
        api_key=api_key,
        temperature=temperature,
    )
