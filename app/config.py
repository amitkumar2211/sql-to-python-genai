# app/config.py

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Google Cloud project settings
GCP_PROJECT = os.getenv("GCP_PROJECT")
GCP_REGION = os.getenv("GCP_REGION")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Gemini model settings
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
DEFAULT_FRAMEWORK = "pandas"

# Prompt tuning
TEMPERATURE = 0.2
MAX_TOKENS = 2048