# ollama_example.py
# Queries a locally running Ollama model via its REST API
# Make sure Ollama is installed: https://ollama.ai/
# Pull a model first: ollama pull llama3.2

import requests

# Ollama runs locally — no API key needed
OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "llama3.2"  # Updated model name


def query_ollama(prompt):
    """Query the local Ollama model with a user prompt."""
    try:
        url = f"{OLLAMA_BASE_URL}/api/chat"  # Updated endpoint
        payload = {
            "model": MODEL_NAME,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        }
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure it is running."
    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    print(f"Using local Ollama model: {MODEL_NAME}")
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Ollama (local)...")
    result = query_ollama(user_prompt)
    print("\nResponse:")
    print(result)
