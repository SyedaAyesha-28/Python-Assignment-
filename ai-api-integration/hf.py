# huggingface_example.py
# Queries Hugging Face using InferenceClient with provider="auto"
# provider="auto" picks the best FREE provider available for the model.
# Install: pip install huggingface_hub
# Get your token at: https://huggingface.co/settings/tokens

import os
from huggingface_hub import InferenceClient

# Configure API - reads from environment variable
api_key = os.getenv("HUGGINGFACE_API_KEY")
if not api_key:
    raise ValueError("HUGGINGFACE_API_KEY environment variable not set.")

# This model is freely routed via Sambanova/Nebius/Together on HF
MODEL_ID = "Qwen/Qwen2.5-72B-Instruct"

# provider="auto" lets HF pick the best available free provider automatically
client = InferenceClient(
    provider="auto",
    api_key=api_key,
)


def query_huggingface(prompt):
    """Query the Hugging Face Inference API with a user prompt."""
    try:
        response = client.chat_completion(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    print(f"Using Hugging Face model: {MODEL_ID}")
    print("(Routed automatically to a free inference provider)")
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Hugging Face API...")
    result = query_huggingface(user_prompt)
    print("\nResponse:")
    print(result)
