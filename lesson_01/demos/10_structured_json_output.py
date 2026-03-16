"""Structured output -- LLM zwraca JSON z konkretnymi kluczami które możesz odczytać."""

import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# ============================================================
# Podejscie 1: response_format = json_object
# Prosimy LLM zeby zwrocil JSON -- dziala ale nie gwarantuje schematu
# ============================================================
print("=" * 50)
print("Podejście 1: response_format = json_object")
print("=" * 50)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Always respond in JSON format.",
        },
        {
            "role": "user",
            "content": "Give me 3 fictional book recommendations. "
            "For each include: title, author, genre, and a one-sentence description.",
        },
    ],
    response_format={"type": "json_object"},  # <-- wymuszamy JSON
)

raw_json = response.choices[0].message.content
print(f"Surowy JSON z API:\n{raw_json}\n")

# Parsujemy JSON i odczytujemy poszczegolne klucze
data = json.loads(raw_json)
print("Odczytane dane:")

# Struktura moze byc rozna -- LLM decyduje o kluczach
# Najczesciej zwraca cos w stylu {"books": [...]} albo {"recommendations": [...]}
books_key = next(iter(data))  # bierzemy pierwszy klucz
books = data[books_key]

for i, book in enumerate(books, 1):
    print(f"\n  Książka {i}:")
    print(f"    Tytuł:  {book.get('title', 'brak')}")
    print(f"    Autor:  {book.get('author', 'brak')}")
    print(f"    Gatunek: {book.get('genre', 'brak')}")
    print(f"    Opis:   {book.get('description', 'brak')}")


# ============================================================
# Podejscie 2: JSON Schema (structured output) -- GWARANTOWANY schemat
# LLM MUSI zwrocic dokladnie ta strukture ktora definiujemy
# ============================================================
print("\n" + "=" * 50)
print("Podejście 2: JSON Schema -- gwarantowany schemat")
print("=" * 50)

# Definiujemy dokladny schemat odpowiedzi
json_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "movie_recommendations",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "movies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "Movie title",
                            },
                            "year": {
                                "type": "integer",
                                "description": "Release year",
                            },
                            "genre": {
                                "type": "string",
                                "description": "Primary genre",
                            },
                            "rating": {
                                "type": "number",
                                "description": "Rating out of 10",
                            },
                            "why_watch": {
                                "type": "string",
                                "description": "One sentence why you should watch it",
                            },
                        },
                        "required": ["title", "year", "genre", "rating", "why_watch"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["movies"],
            "additionalProperties": False,
        },
    },
}

response2 = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
    messages=[
        {
            "role": "user",
            "content": "Recommend 3 sci-fi movies from the 2000s.",
        },
    ],
    response_format=json_schema,  # <-- wymuszamy dokladny schemat
)

raw_json2 = response2.choices[0].message.content
data2 = json.loads(raw_json2)

print(f"Surowy JSON:\n{raw_json2}\n")

# Teraz mamy GWARANCJE ze klucze istnieja -- mozemy smialo odczytywac
print("Odczytane dane (gwarantowany schemat):")
for movie in data2["movies"]:
    print(f"\n  🎬 {movie['title']} ({movie['year']})")
    print(f"     Gatunek: {movie['genre']}")
    print(f"     Ocena:   {movie['rating']}/10")
    print(f"     Obejrzyj bo: {movie['why_watch']}")

# ============================================================
# Praktyczny przyklad: Ekstrakcja danych z tekstu
# ============================================================
print("\n" + "=" * 50)
print("Praktyczny przykład: Ekstrakcja danych z tekstu")
print("=" * 50)

extract_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "contact_extraction",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "contacts": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "email": {"type": "string"},
                            "company": {"type": "string"},
                            "role": {"type": "string"},
                        },
                        "required": ["name", "email", "company", "role"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["contacts"],
            "additionalProperties": False,
        },
    },
}

messy_text = """
Hey, I met some cool people at the conference yesterday. 
Anna Kowalska from TechCorp (she's their CTO) gave me her card - anna.k@techcorp.com.
Also talked to Bob Smith, he does ML engineering at DataFlow Inc, his email is bob@dataflow.io.
Oh and Maria Garcia from StartupXYZ (CEO) - maria@startupxyz.com - super interesting pitch.
"""

response3 = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
    messages=[
        {
            "role": "system",
            "content": "Extract contact information from the text.",
        },
        {"role": "user", "content": messy_text},
    ],
    response_format=extract_schema,
)

contacts = json.loads(response3.choices[0].message.content)

print(f"Tekst wejsciowy:\n{messy_text}")
print("Wyekstrahowane kontakty:")
for c in contacts["contacts"]:
    print(f"  {c['name']} | {c['role']} @ {c['company']} | {c['email']}")

print("\n" + "=" * 50)
print("Kluczowe wnioski:")
print("  1. json_object -- LLM zwraca JSON, ale TY nie kontrolujesz schematu")
print("  2. json_schema -- GWARANTUJESZ schemat, LLM MUSI sie dostosowac")
print("  3. Structured output to fundament: agenty, pipelines, integracje")
print("  4. Zawsze uzywaj json.loads() do parsowania -- nigdy eval()!")
