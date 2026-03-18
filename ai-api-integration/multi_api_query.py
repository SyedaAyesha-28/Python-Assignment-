# multi_api_query.py
# Unified program to query multiple AI providers from one interface
# Supports: Groq, Ollama, Hugging Face, Google Gemini, Cohere

import os
import requests

# ── Optional imports ────────────────────────────────────────────────────────
try:
    from groq import Groq
except ImportError:
    Groq = None

try:
    from google import genai as google_genai
except ImportError:
    google_genai = None

try:
    import cohere
except ImportError:
    cohere = None

try:
    from huggingface_hub import InferenceClient
except ImportError:
    InferenceClient = None


# ── Provider query functions ─────────────────────────────────────────────────

def query_groq(prompt):
    """Query Groq LLaMA model."""
    if Groq is None:
        return "Error: groq package not installed. Run: pip install groq"
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Error: GROQ_API_KEY not set."
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def query_ollama(prompt):
    """Query local Ollama model."""
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3.2",
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
            },
            timeout=120,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    except requests.exceptions.ConnectionError:
        return "Error: Ollama not running."
    except Exception as e:
        return f"Error: {str(e)}"


def query_huggingface(prompt):
    """Query Hugging Face via SambaNova provider."""
    if InferenceClient is None:
        return "Error: huggingface_hub not installed. Run: pip install huggingface_hub"
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        return "Error: HUGGINGFACE_API_KEY not set."
    try:
        client = InferenceClient(provider="auto", api_key=api_key)
        response = client.chat_completion(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def query_gemini(prompt):
    """Query Google Gemini."""
    if google_genai is None:
        return "Error: google-genai not installed. Run: pip install google-genai"
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY not set."
    try:
        client = google_genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


def query_cohere(prompt):
    """Query Cohere."""
    if cohere is None:
        return "Error: cohere not installed. Run: pip install cohere"
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        return "Error: COHERE_API_KEY not set."
    try:
        client = cohere.ClientV2(api_key=api_key)
        response = client.chat(
            model="command-a-03-2025",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"


# ── Provider registry ────────────────────────────────────────────────────────

PROVIDERS = {
    "1": ("Groq (LLaMA 3.3 70B)",           query_groq),
    "2": ("Ollama (local LLaMA 3.2)",        query_ollama),
    "3": ("Hugging Face (Qwen 2.5 72B)",     query_huggingface),
    "4": ("Google Gemini 2.0 Flash",         query_gemini),
    "5": ("Cohere (Command-A 03-2025)",      query_cohere),
}


# ── Main execution ────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("       Multi-API Query Tool")
    print("=" * 50)
    print("Select an AI provider:")
    for key, (name, _) in PROVIDERS.items():
        print(f"  {key}. {name}")
    print("  0. Query ALL providers and compare")
    print("-" * 50)

    choice = input("Enter choice (0-5): ").strip()

    if choice not in PROVIDERS and choice != "0":
        print("Invalid choice. Exiting.")
        return

    user_prompt = input("Enter your prompt: ").strip()
    if not user_prompt:
        print("Empty prompt. Exiting.")
        return

    if choice == "0":
        print("\n" + "=" * 50)
        print("Querying ALL providers...")
        print("=" * 50)
        for key, (name, fn) in PROVIDERS.items():
            print(f"\n[{name}]")
            print("-" * 40)
            result = fn(user_prompt)
            print(result)
        print("\n" + "=" * 50)
    else:
        name, fn = PROVIDERS[choice]
        print(f"\nQuerying {name}...")
        print("-" * 40)
        result = fn(user_prompt)
        print("\nResponse:")
        print(result)


if __name__ == "__main__":
    main()
