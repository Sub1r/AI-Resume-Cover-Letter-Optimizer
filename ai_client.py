import requests


def get_ai_response(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data["response"]
    else:
        return "Error: Could not get response from Ollama."