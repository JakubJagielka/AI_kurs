"""Generowanie wektora embedding -- tak komputery rozumieja znaczenie tekstu."""

import os
import numpy as np
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)


def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )
    return response.data[0].embedding


def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Generujemy embeddingi dla roznych zdan
sentences = [
    "The happy dog played in the park",
    "A cheerful puppy ran around the garden",
    "Quantum physics describes subatomic particles",
]

embeddings = [get_embedding(s) for s in sentences]

print(f"Wymiar embeddingu: {len(embeddings[0])}")
print(f"Pierwsze 10 wartosci: {embeddings[0][:10]}")
print()

# Porownujemy podobienstwa
for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        sim = cosine_similarity(embeddings[i], embeddings[j])
        print(f'"{sentences[i][:40]}..." vs "{sentences[j][:40]}..."')
        print(f"  Podobienstwo: {sim:.4f}")
        print()
