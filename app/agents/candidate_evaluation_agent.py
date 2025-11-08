import google.generativeai as genai
from dotenv import load_dotenv
import os
from app.prompts import CANDIDATE_EVALUATION
import json
import time

# Load environment variables from .env file
load_dotenv()
# Initialize Google Gemini client with API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def evaluate_candidate(candidate_details: str, jd: str) -> str:
    """
    Function to analyze the extracted text from a resume using Google Gemini API.
    """
    if not api_key:
        return {"error": "Google API key not set"}
    prompt = CANDIDATE_EVALUATION.format(resume_json=candidate_details, jd_json=jd)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            model = genai.GenerativeModel("gemini-2.0-flash-exp")
            response = model.generate_content(prompt)
            text = response.text.strip()
            if text.startswith('```json'):
                text = text[7:]
            if text.endswith('```'):
                text = text[:-3]
            text = text.strip()
            print("Response from Google Gemini API:", text)
            return text
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"Rate limit exceeded, retrying in {wait_time} seconds... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
            else:
                return {"error": str(e)}
