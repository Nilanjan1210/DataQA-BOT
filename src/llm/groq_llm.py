from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


load_dotenv()
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in the environment variables")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def llm(model = "openai/gpt-oss-120b", temperature = 0, **kwargs):
    return ChatGroq(
        model=model,
        temperature=temperature,
        api_key=GROQ_API_KEY,
        **kwargs
    )

result = llm().invoke("Hello, how are you?")
print(result.content)