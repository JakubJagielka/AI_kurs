# Lekcja 1 -- Cwiczenia

## Cwiczenia podstawowe

### 1. Eksplorator temperatury
Wez `01_first_llm_call.py` i odpal ten sam prompt z temperaturami: 0, 0.5, 1.0, 1.5.
Zapisz kazdy output. Co zauwazylas/es? Kiedy uzylbys kazdej wartosci?

### 2. Wyzwanie Vision
Uzyj `02_vision_api.py` do analizy 3 roznych obrazkow (znajdz URL-e online).
Sprobuj: wykres, mema, zdjecie jedzenia. Jak dobrze model radzi sobie z kazdym?

### 3. Detektyw embeddingowy
Uzywajac `04_embeddings_intro.py`, wygeneruj embeddingi dla tych zdan:
- "The cat sat on the mat"
- "A feline rested on the rug"
- "Stock markets crashed today"

Oblicz cosine similarity miedzy kazda para. Ktore dwa sa najbardziej podobne? Dlaczego?

### 4. Prompt Engineering
Zmodyfikuj `01_first_llm_call.py` zeby:
- Napisal haiku o programowaniu
- Wyjasnil komputery kwantowe 5-latkowi
- Wygenerowl obiekt JSON z 3 fikcyjnymi tytulami ksiazek + autorami

Jaki system prompt dziala najlepiej dla kazdego zadania?

### 5. Structured JSON Output
Uzyj `10_structured_json_output.py` jako punkt wyjscia:
- Zdefiniuj wlasny `json_schema` ktory ekstrrahuje **pozycje z paragonu** (nazwa produktu, ilosc, cena)
- Podaj LLM-owi tekst: "Kupilem 2 chleby po 4.50, maslo za 7.99 i 3 jogurty po 2.30"
- Odczytaj klucze z JSON-a i oblicz suma zakupow w Pythonie
- Bonus: dodaj pole `category` (np. "pieczywo", "nabiał") i zobacz czy LLM poprawnie je przypisze

### 6. Eksperyment z Function Calling
Rozszerz `06_function_calling_intro.py` o drugie narzedzie — np. `get_time()` zwracajace aktualny czas.
Zapytaj model "What's the weather AND what time is it?" — czy wywola oba narzedzia?

---

## Zaawansowane

### 6. Starcie providerow
Uzyj `09_multi_provider_compare.py` zeby porownac Azure OpenAI i Gemini na:
- Kreatywnym prompcie pisarskim
- Zadaniu generowania kodu
- Pytaniu o fakty

Ktory model wygrywa w kazdym? Jest jeden wyrazny zwyciezca?

### 7. Czat z pamięcią -- limity
Uzyj `08_chat_with_memory.py` i przeprowadz dluga rozmowe (10+ wiadomosci).
- Ile wiadomosci jest w `conversation_history` na koniec?
- Zmodyfikuj kod zeby wyswietlal **liczbe tokenow** (przyblizona: `len(str(conversation_history)) // 4`)
- Dodaj **okno pamięci**: Trzymaj tylko ostatnie N wiadomosci (np. 6) + system prompt. Co sie stanie gdy zapytasz o cos z wczesniejszej czesci rozmowy?
- Dyskusja: Jak rozwiazalbys ten problem w produkcji? (Podpowiedz: podsumowanie starszych wiadomosci)

### 8. Zbuduj wlasne narzedzie
Stworz nowe demo function calling gdzie LLM ma dostep do narzedzia `translate(text, target_language)`.
Test: "How do you say 'hello world' in Japanese?"
