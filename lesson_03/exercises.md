# Lekcja 3 -- Cwiczenia (cele dodatkowe dla Projektu 2)

## Podstawowe (rob na zajeciach jesli starczy czasu)

### 1. Porownanie modeli
Sprobuj generowac menu roznymi modelami Ollama:
- `llama3.2:3b`
- `qwen2.5:3b`
- `mistral:7b` (jesli twoja maszyna da rade)

Porownaj: jakosc outputu, szybkosc, niezawodnosc formatowania JSON.
Ktory model jest najlepszy do strukturyzowanego generowania menu?

### 2. Kreatywne motywy
Przetestuj swoj generator menu z nietypowymi motywami:
- "Restauracja na Marsie"
- "Sredniowieczna tawerna serwujaca nowoczesna kuchnie fusion"
- "Kocia kawiarnia gdzie koty sa szefami kuchni"

Czy LLM dobrze radzi sobie z kreatywnymi promptami? Co sie psuje?

### 3. Lepsze prompty do obrazkow
Zamiast uzywac samej nazwy dania do generowania obrazka, stworz lepszy prompt:
- Dolacz styl kuchni
- Dodaj "food photography, appetizing, restaurant quality"
- Wspomnij o podaniu i oswietleniu

Porownaj jakosc obrazkow z prostym vs szczegolowym promptem.

---

## Zaawansowane

### 4. Filtry dietetyczne
Dodaj funkcje: uzytkownicy moga okreslic ograniczenia dietetyczne (vegan, bezglutenowe itp.).
System prompt powinien zapewnic ze wszystkie wygenerowane pozycje spelniaja wymagania.
Jak zweryfikujesz czy LLM faktycznie postuchal?

### 5. Menu wielojezyczne
Wygeneruj to samo menu w wielu jezykach.
Uzyj albo:
- Ollama z wielojezycznym modelem
- Pipeline tlumaczenia HuggingFace
- Drugiego wywolania LLM-a do tlumaczenia

### 6. Lokalne generowanie obrazkow
Jesli masz przyzwoita maszyne, sprobuj zamienic DALL-E na lokalny model:
- Zainstaluj biblioteke `diffusers`
- Uzyj malego modelu Stable Diffusion
- Porownaj szybkosc i jakosc z DALL-E

Uwaga: Na CPU bedzie WOLNE. O to chodzi -- zrozum kompromis.
