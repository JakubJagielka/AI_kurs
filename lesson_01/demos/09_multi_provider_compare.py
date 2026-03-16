"""Zaawansowane: Ten sam prompt, rozni providerzy -- Azure OpenAI vs Gemini."""

import os
import time
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

PROMPT = "Explain recursion in 3 sentences. Include a real-world analogy."


def call_azure_openai(prompt: str) -> tuple[str, float]:
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2024-12-01-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )
    start = time.time()
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    elapsed = time.time() - start
    return response.choices[0].message.content, elapsed


def call_gemini(prompt: str) -> tuple[str, float]:
    """Gemini przez OpenAI-kompatybilny endpoint."""
    try:
        import google.generativeai as genai

        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-2.0-flash")

        start = time.time()
        response = model.generate_content(prompt)
        elapsed = time.time() - start
        return response.text, elapsed
    except Exception as e:
        return f"Gemini niedostepny: {e}", 0.0


# Odpalamy oba
print(f"Prompt: {PROMPT}\n")

print("=" * 50)
print("AZURE OPENAI (gpt-5.3-chat)")
print("=" * 50)
azure_response, azure_time = call_azure_openai(PROMPT)
print(azure_response)
print(f"\nCzas: {azure_time:.2f}s")

print()

print("=" * 50)
print("GOOGLE GEMINI")
print("=" * 50)
gemini_response, gemini_time = call_gemini(PROMPT)
print(gemini_response)
print(f"\nCzas: {gemini_time:.2f}s")

print("\nNie ma jednego najlepszego modelu. Wybieraj na podstawie: zadania, szybkosci, kosztu, wymaganej jakosci.")
