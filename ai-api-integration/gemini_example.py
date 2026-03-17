# gemini_example.py
# Queries Google Gemini using the NEW google-genai package
# Old package (google.generativeai) is deprecated — use google-genai instead
# Install: pip install google-genai
# Get your API key at: https://aistudio.google.com/app/apikey

import os
from google import genai

# Configure API - reads from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

# Initialize the new Gemini client
client = genai.Client(api_key=api_key)


def query_gemini(prompt):
    """Query the Google Gemini API with a user prompt."""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    print("Using Google Gemini (gemini-2.0-flash)")
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Google Gemini API...")
    result = query_gemini(user_prompt)
    print("\nResponse:")
    print(result)
