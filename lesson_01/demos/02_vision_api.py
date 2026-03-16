"""Wyslij obrazek do multimodalnego modelu i dostaniesz opis."""

import os
import base64
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg"

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What do you see in this image? Be specific."},
                {"type": "image_url", "image_url": {"url": IMAGE_URL}},
            ],
        }
    ],
)

print(response.choices[0].message.content)

# --- Sprobuj sam ---
# Podmien IMAGE_URL na dowolny URL obrazka. Sprobuj wykres, mema, screenshot.
