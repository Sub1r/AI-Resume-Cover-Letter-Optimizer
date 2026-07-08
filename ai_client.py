import requests


def get_ai_response(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Ollama returned status code {response.status_code}."
            )

        data = response.json()

        if "response" not in data:
            raise RuntimeError(
                "Invalid response received from Ollama."
            )

        return data["response"]

    except requests.exceptions.RequestException as e:
        raise RuntimeError(
            "Unable to connect to Ollama."
        ) from e