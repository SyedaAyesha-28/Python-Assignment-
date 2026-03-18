# AI API Integration

A collection of Python programs that demonstrate how to query multiple Generative AI providers from the command line.

> **Note:** OpenAI is excluded from this submission as per instructor instructions.

---

## Providers Covered

| File | Provider | Model Used |
|------|----------|------------|
| `groq_example.py` | Groq | LLaMA 3.3 70B Versatile |
| `ollama_example.py` | Ollama (local) | LLaMA 3.2 (runs offline) |
| `hf.py` | Hugging Face | Qwen 2.5 72B (via SambaNova) |
| `gemini_example.py` | Google Gemini | Gemini 2.0 Flash |
| `cohere_example.py` | Cohere | Command-A 03 2025 |
| `multi_api_query.py` | All of the above | Select at runtime |

---

## Project Structure

```
ai-api-integration/
├── groq_example.py
├── ollama_example.py
├── hf_example.py
├── gemini_example.py
├── cohere_example.py
├── multi_api_query.py        # Bonus: query any/all providers
├── requirements.txt
├── README.md
└── screenshots/
    ├── groq_output.png
    ├── ollama_output.png
    ├── huggingface_output.png
    ├── gemini_output.png
    └── cohere_output.png
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ai-api-integration
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

For Ollama, download and install from https://ollama.ai/ then pull a model:
```bash
ollama pull llama3.2
```

### 3. Set environment variables

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your-groq-key-here
set HUGGINGFACE_API_KEY=your-hf-token-here
set GOOGLE_API_KEY=your-google-key-here
set COHERE_API_KEY=your-cohere-key-here
```

**Linux / macOS:**
```bash
export GROQ_API_KEY="your-groq-key-here"
export HUGGINGFACE_API_KEY="your-hf-token-here"
export GOOGLE_API_KEY="your-google-key-here"
export COHERE_API_KEY="your-cohere-key-here"
```

> ⚠️ Never hardcode API keys in your source code or commit them to GitHub.

---

## How to Obtain Each API Key

| Provider | URL |
|----------|-----|
| Groq | https://console.groq.com/ → API Keys |
| Hugging Face | https://huggingface.co/settings/tokens |
| Google Gemini | https://aistudio.google.com/app/apikey |
| Cohere | https://dashboard.cohere.com/ → API Keys |
| Ollama | No key needed — runs locally |

### Hugging Face Extra Step
After getting your token, enable a free inference provider:
1. Go to https://huggingface.co/settings/inference-providers
2. Enable **SambaNova** (free)

---

## How to Run Each Program

```bash
# Groq
python groq_example.py

# Ollama (runs locally, no API key needed)
python ollama_example.py

# Hugging Face
python hf.py

# Google Gemini
python gemini_example.py

# Cohere
python cohere_example.py

# Bonus: query any or all providers at once
python multi_api_query.py
```

---

## Bonus Features

### multi_api_query.py
A unified program that lets you:
- Select which AI provider to use (1-5)
- Or query **ALL providers at once** (option 0) to compare responses side by side

---

## Screenshots

See the `screenshots/` folder for sample output from each provider.

---

## Notes

- Ollama runs entirely **offline** — no API key or internet needed after model is pulled.
- Google's `google.generativeai` package is deprecated — this project uses the new `google-genai` package.
- Hugging Face deprecated free LLM inference in 2025 — this project uses `huggingface_hub` with `provider="auto"` which routes to free providers like SambaNova.
