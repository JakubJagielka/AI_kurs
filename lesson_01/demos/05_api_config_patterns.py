"""Wzorce konfiguracji API -- jak profesjonalisci ustawiaja klienty LLM."""

import os
import time
from openai import AzureOpenAI, APIError, RateLimitError
from dotenv import load_dotenv

load_dotenv()

# --- Wzorzec 1: Konfiguracja przez zmienne srodowiskowe ---
# Nigdy nie hardkoduj kluczy API. Uzyj plikow .env + zmiennych srodowiskowych.

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    timeout=30.0,       # nie czekaj w nieskonczonosc
    max_retries=3,      # wbudowany retry (SDK to ogarnia)
)


# --- Wzorzec 2: Retry z backoffem dla wlasnej logiki ---

def call_llm_with_retry(messages: list, max_attempts: int = 3) -> str:
    for attempt in range(max_attempts):
        try:
            response = client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
                messages=messages,
                temperature=0.7,
            )
            return response.choices[0].message.content

        except RateLimitError:
            wait = 2 ** attempt  # exponential backoff: 1s, 2s, 4s
            print(f"Rate limit. Czekam {wait}s przed ponowieniem...")
            time.sleep(wait)

        except APIError as e:
            print(f"Blad API: {e}. Proba {attempt + 1}/{max_attempts}")
            if attempt == max_attempts - 1:
                raise

    raise Exception("Wszystkie proby sie nie powiodly")


# --- Wzorzec 3: Wybor modelu ---

def call_model(prompt: str, model: str = None) -> str:
    """Uzywaj roznych modeli do roznych zadan."""
    model = model or os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat")

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


# Demo
result = call_llm_with_retry([
    {"role": "system", "content": "Be concise."},
    {"role": "user", "content": "What's the capital of France?"},
])
print(result)
