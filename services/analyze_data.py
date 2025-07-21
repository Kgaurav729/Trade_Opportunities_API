import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

GEMINI_API_KEY = os.getenv("your-gemini-api-key")


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_sector_news(sector: str, news_data: List[str]) -> str:
    if not news_data:
        return "No relevant news data found to analyze."

    prompt = f"""
You are a market analyst. Analyze the following news headlines related to the Indian {sector} sector. 
Generate a brief summary of current trends, risks, and trade opportunities in markdown format.

News Articles:
{chr(10).join(f"- {item}" for item in news_data)}

Provide structured output:
### Sector Overview
...
### Current Trends
...
### Trade Opportunities
...
### Risks
...
    """

    response = model.generate_content(prompt)
    return response.text
