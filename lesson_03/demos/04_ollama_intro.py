"""Ollama intro -- lokalny LLM z tym samym wzorcem API co OpenAI."""

import ollama

# Upewnij sie ze Ollama dziala i pobrales model:
#   ollama pull llama3.2:3b

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Be concise."},
        {"role": "user", "content": "What is Python? Answer in 2 sentences."},
    ],
)

print(response["message"]["content"])

print("\n" + "=" * 50)
print("Strukturyzowany output (tryb JSON):")
print("=" * 50)

# Tryb JSON -- ten sam koncept co response_format w OpenAI
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Always respond in valid JSON.",
        },
        {
            "role": "user",
            "content": 'Give me 3 fun facts about cats. Format: {"facts": ["...", "...", "..."]}',
        },
    ],
    format="json",
)

print(response["message"]["content"])

# --- Sprobuj sam ---
# Przetestuj rozne modele: ollama pull qwen2.5:3b, ollama pull mistral:7b
# Porownaj szybkosc i jakosc. Ktory jest lepszy do twojego zadania?
