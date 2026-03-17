# cohere_example.py
# Queries Cohere's language models using the cohere Python SDK
# Install: pip install cohere
# Get your API key at: https://dashboard.cohere.com/

import os
import cohere

# Configure API - reads from environment variable
api_key = os.getenv("COHERE_API_KEY")
if not api_key:
    raise ValueError("COHERE_API_KEY environment variable not set.")

# Initialize Cohere client
client = cohere.ClientV2(api_key=api_key)


def query_cohere(prompt):
    """Query the Cohere API with a user prompt."""
    try:
        response = client.chat(
            model="command-a-03-2025",   # Latest Cohere model (command-r removed Sep 2025)
            messages=[{"role": "user", "content": prompt}],
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    print("Using Cohere (command-a-03-2025)")
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Cohere API...")
    result = query_cohere(user_prompt)
    print("\nResponse:")
    print(result)
