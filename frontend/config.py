# config.py
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env if present

BACKEND_URL: str = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
HF_API_KEY: Optional[str] = os.getenv("HF_API_KEY")
PORCUPINE_KEY: Optional[str] = os.getenv("PORCUPINE_KEY")