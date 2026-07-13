# Part 4 – Intelligent LLM System with Production Guardrails

## Objective

Build a production-conscious AI application using a Large Language Model (LLM) with basic guardrails.

## Features

- Reads API key securely from `.env`
- Sends HTTP POST request to an LLM API
- Returns structured JSON output
- Input validation
- Exception handling
- Logging
- Timeout protection

## Production Guardrails

- Rejects empty input
- Rejects inputs longer than 500 characters
- Handles API timeouts
- Handles HTTP errors
- Handles invalid JSON responses
- Stores logs in `app.log`

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

## Run

```bash
python app.py
```

## Example Output

```json
{
    "question": "What is Artificial Intelligence?",
    "answer": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "confidence": "High"
}
```

## Design Decisions

- Uses the OpenAI Responses API.
- API keys are never stored in source code.
- Structured JSON makes the output easy to parse.
- Logging helps with debugging.
- Input validation improves reliability.
- Error handling prevents crashes due to API failures or invalid responses.
