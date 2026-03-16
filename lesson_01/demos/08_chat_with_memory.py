"""Czat z pamięcią konwersacji -- LLM pamięta co powiedzieliśmy wcześniej."""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Historia konwersacji -- to jest caly "trik". LLM nie ma pamieci sam z siebie.
# My musimy za kazdym razem wysylac CALA dotychczasowa rozmowe.
conversation_history = [
    {
        "role": "system",
        "content": "You are a friendly assistant who remembers everything the user tells you. "
        "Refer back to earlier parts of the conversation when relevant.",
    },
]


def chat(user_message: str) -> str:
    """Wyslij wiadomosc do LLM z calą historią konwersacji."""
    # Dodajemy nowa wiadomosc uzytkownika do historii
    conversation_history.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
        messages=conversation_history,  # <-- CALA historia leci do API
        temperature=0.7,
    )

    assistant_message = response.choices[0].message.content

    # Dodajemy odpowiedz asystenta do historii -- zeby tez byla w nastepnym uzyciu
    conversation_history.append({"role": "assistant", "content": assistant_message})

    return assistant_message


# --- Demo: Interaktywny czat ---
print("Czat z pamięcią konwersacji (wpisz 'quit' zeby wyjsc)")
print("=" * 50)
print("Sprobuj: powiedz jak masz na imie, potem zapytaj 'jak mam na imie?'\n")

while True:
    user_input = input("Ty: ").strip()
    if user_input.lower() in ("quit", "exit", "q"):
        break
    if not user_input:
        continue

    response = chat(user_input)
    print(f"AI: {response}\n")

# Pokaz historie na koniec
print("\n" + "=" * 50)
print(f"Laczna liczba wiadomosci w historii: {len(conversation_history)}")
print("Historia konwersacji (to idzie do API za kazdym razem):")
for msg in conversation_history:
    role = msg["role"].upper()
    content = msg["content"][:80] + "..." if len(msg["content"]) > 80 else msg["content"]
    print(f"  [{role}] {content}")

print("\nKluczowy wniosek: LLM NIE ma wbudowanej pamieci.")
print("To MY przechowujemy historie i wysylamy ja za kazdym razem.")
print("Dlatego dlugie konwersacje zuzywa wiecej tokenow (= wiecej kosztuja).")
