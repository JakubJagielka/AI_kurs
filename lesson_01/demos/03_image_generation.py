"""Generowanie obrazu z prompta tekstowego przez DALL-E."""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

response = client.images.generate(
    model="dall-e-3",
    prompt="A cozy coffee shop on a rainy day, watercolor style",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(f"URL obrazka: {image_url}")
print("Otworz ten URL w przegladarce zeby zobaczyc wynik!")

# --- Sprobuj sam ---
# Zmien prompt. Przetestuj rozne style: "pixel art", "oil painting", "photograph".
