import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_api_key():
    return os.getenv("GEMINI_API_KEY")