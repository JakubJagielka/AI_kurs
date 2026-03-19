"""Generowanie wektora embedding -- tak komputery rozumieja znaczenie tekstu."""

import numpy as np
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def get_embedding(text: str) -> list[float]:
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
    )
    return result.embeddings[0].values


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
