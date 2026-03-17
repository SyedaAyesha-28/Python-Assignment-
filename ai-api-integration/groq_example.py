# groq_example.py
# Queries Groq's LLaMA models using the Groq Python SDK
# Install: pip install groq
# Get your API key at: https://console.groq.com/

import os
from groq import Groq

# Configure API - reads from environment variable
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set.")

# Initialize Groq client
client = Groq(api_key=api_key)


def query_groq(prompt):
    """Query the Groq API with a user prompt."""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Updated model (llama3-8b-8192 decommissioned)
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Groq API...")
    result = query_groq(user_prompt)
    print("\nResponse:")
    print(result)
