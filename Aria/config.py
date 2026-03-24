from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Missing GROQ_API_KEY")

client = Groq(api_key=api_key)

MODEL_NAME = "llama-3.3-70b-versatile"