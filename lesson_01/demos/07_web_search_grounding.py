"""Web search grounding -- LLM-y nie znaja dzisiejszych wiadomosci, ale mozesz dac im narzedzia ktore znaja."""

import os
from google import genai
from google.genai import types
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

azure_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Najpierw: pytamy bez groundingu -- LLM odmowi albo zhallucynuje
print("=== Bez web search (Azure OpenAI) ===")
response = azure_client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
    messages=[
        {"role": "user", "content": "What are today's top tech news headlines?"},
    ],
)
print(response.choices[0].message.content)
print()

# Teraz: z web search groundingiem przez Gemini + Google Search
# Gemini ma wbudowane narzedzie Google Search -- nie wymaga osobnej konfiguracji!
print("=== Z Google Search groundingiem (Gemini) ===")
try:
    gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    config = types.GenerateContentConfig(
        tools=[grounding_tool]
    )

    response = gemini_client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="What are today's top tech news headlines?",
        config=config,
    )

    print(response.text)
except Exception as e:
    print(f"Gemini Google Search nie zadziałał: {e}")
    print("Sprawdz czy GEMINI_API_KEY jest ustawiony w pliku .env")

print()
print("Kluczowy wniosek: LLM-y same z siebie NIE wiedza co sie dzieje dzisiaj.")
print("Musisz dac im narzedzie (Google Search, Bing, itp.) zeby mogly sprawdzic.")
