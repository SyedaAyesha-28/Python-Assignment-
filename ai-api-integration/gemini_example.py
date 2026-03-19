# gemini_example.py
# Queries Google Gemini using the google-genai package
# Install: pip install google-genai
# Get your API key at: https://aistudio.google.com/app/apikey

import os
from google import genai

# Configure API - reads from environment variable
# Note: google-genai accepts both GOOGLE_API_KEY and GEMINI_API_KEY
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

# Initialize the Gemini client
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
        # Try fallback model if main one fails
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite",
                contents=prompt,
            )
            return response.text
        except Exception as e2:
            return f"Error: {str(e2)}"


# Main execution
if __name__ == "__main__":
    print("Using Google Gemini (gemini-2.0-flash)")
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Google Gemini API...")
    result = query_gemini(user_prompt)
    print("\nResponse:")
    print(result)
