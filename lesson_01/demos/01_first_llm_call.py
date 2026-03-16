"""Pierwsze wywolanie LLM -- generowanie tekstu z Azure OpenAI."""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain what an API is in 3 sentences."},
    ],
)

print(response.choices[0].message.content)

# --- Sprobuj sam ---
# Zmien wiadomosc usera, temperature, system prompt. Zobacz co sie zmieni.
