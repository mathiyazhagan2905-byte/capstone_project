import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

URL = "https://api.openai.com/v1/responses"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

user_text = input("Enter your question: ")

payload = {
    "model": "gpt-4.1-mini",
    "input": f"""
Return ONLY valid JSON.

Question:
{user_text}

Format:
{{
  "question": "...",
  "summary": "...",
  "keywords": ["...","...","..."]
}}
"""
}

response = requests.post(URL, headers=headers, json=payload)

if response.status_code == 200:
    result = response.json()

    output_text = result["output"][0]["content"][0]["text"]

    structured = json.loads(output_text)

    print("\nStructured Output")
    print(json.dumps(structured, indent=4))

else:
    print("Error:", response.status_code)
    print(response.text)