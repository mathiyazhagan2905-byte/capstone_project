import os
import json
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

URL = "https://api.openai.com/v1/responses"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def validate_input(text):
    """Basic input validation."""
    if len(text.strip()) == 0:
        return False, "Input cannot be empty."

    if len(text) > 500:
        return False, "Input exceeds 500 characters."

    return True, ""


def build_prompt(user_input):
    return f"""
You are a helpful AI assistant.

Return ONLY valid JSON.

Question:
{user_input}

Format:
{{
    "question":"...",
    "answer":"...",
    "confidence":"High"
}}
"""


def ask_llm(question):

    payload = {
        "model": "gpt-4.1-mini",
        "input": build_prompt(question)
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    result = response.json()

    text = result["output"][0]["content"][0]["text"]

    return json.loads(text)


def main():

    print("=== AI Question Answering System ===")

    user_input = input("Ask a question: ")

    valid, message = validate_input(user_input)

    if not valid:
        print(message)
        return

    try:

        output = ask_llm(user_input)

        logging.info(f"Question: {user_input}")

        print("\nAnswer")
        print("----------------------")
        print(json.dumps(output, indent=4))

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

    except json.JSONDecodeError:
        print("Model returned invalid JSON.")

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    main()
