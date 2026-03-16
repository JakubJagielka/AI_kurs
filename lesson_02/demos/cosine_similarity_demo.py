"""Demo cosine similarity -- zobacz jak embeddingi chwytaja znaczenie."""

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


def embed(text: str) -> np.ndarray:
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return np.array(response.data[0].embedding)


def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


sentences = [
    "A happy dog playing in the park",
    "A cheerful puppy running in the garden",
    "The stock market crashed yesterday",
    "A cat sleeping on a warm couch",
    "Global financial markets experienced a downturn",
]

print("Generuje embeddingi...")
embeddings = {s: embed(s) for s in sentences}

print("\nMacierz podobienstwa:")
print("-" * 80)

# Naglowek
print(f"{'':>45}", end="")
for i in range(len(sentences)):
    print(f" [{i}]  ", end="")
print()

for i, s1 in enumerate(sentences):
    label = f"[{i}] {s1[:40]}"
    print(f"{label:>45}", end="")
    for j, s2 in enumerate(sentences):
        sim = cosine_sim(embeddings[s1], embeddings[s2])
        print(f" {sim:.2f} ", end="")
    print()

print()
print("Zwroc uwage: 'happy dog' ~ 'cheerful puppy' (to samo znaczenie, inne slowa)")
print("Zwroc uwage: 'stock market crashed' ~ 'financial downturn' (ten sam koncept)")
print("Zwroc uwage: 'dog' vs 'stock market' = niskie podobienstwo (niepowiazane tematy)")
