import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class llm(ChatGroq):
    def __init__(self):
        super().__init__(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192"
        )
