# app/converter.py

import google.generativeai as genai
from app.config import GEMINI_MODEL, TEMPERATURE, MAX_TOKENS
from dotenv import load_dotenv
import os

load_dotenv()

def init_vertex_ai():
    """Init Gemini via API Key."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing in .env")
    genai.configure(api_key=api_key)

def convert_sql_to_python(sql_code: str, target_framework: str = 'pandas') -> str:
    prompt = f"""
You are a senior data engineer. Convert the following SQL into Python using the {target_framework} framework.
Make sure to retain logic (joins, filters, grouping), use clean syntax, and add helpful comments.

SQL:
{sql_code}

Only return valid Python code.
    """
    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": TEMPERATURE,
            "max_output_tokens": MAX_TOKENS
        }
    )
    return response.text.strip()