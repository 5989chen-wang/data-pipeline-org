import os
from dotenv import load_dotenv
load_dotenv()

LLM_CONFIG = {
    "model": "deepseek-chat",
    "temperature": 0.7,
    "api_key": os.getenv("LLM_API_KEY"),
    "base_url": os.getenv("LLM_BASE_URL", "https://api.deepseek.com/v1"),
}