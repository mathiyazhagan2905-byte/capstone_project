# Part 3 – LLM API Integration

## Objective

Demonstrate how to integrate a Large Language Model using an HTTP POST request and parse structured JSON output.

## Features

- Reads API key from `.env`
- Sends HTTP POST request
- Receives JSON response
- Extracts structured information
- Displays formatted JSON

## Requirements

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

## Example

Input:

```
Explain machine learning
```

Output:

```json
{
  "question": "Explain machine learning",
  "summary": "Machine learning is a branch of AI...",
  "keywords": [
    "AI",
    "Algorithms",
    "Data"
  ]
}
```

## Security

- API keys are stored in `.env`
- `.env` should be added to `.gitignore`
- No secrets are committed to GitHub
