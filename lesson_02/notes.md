# Lekcja 2: AI Engineering -- Projekt 1: Generator PDF + Wyszukiwanie Semantyczne

## Czesc 1 -- Mindset AI i generowanie PDF (~2h)

### Mindset AI Inzyniera
- **Po co AI?** Automatyzacja kreatywnych/powtarzalnych zadan gdzie reguly sa za skomplikowane do zakodowania
- **Co dziala:** Streszczanie, generowanie, klasyfikacja, wyszukiwanie, tlumaczenie
- **Co nie dziala:** Precyzyjna matematyka, dane w real-time, cokolwiek wymagajace 100% dokladnosci
- **Decyzje architektoniczne:** API vs lokalne, framework vs czyste, koszt vs jakosc

### Vibe Coding i odpowiedzialnosc
- AI pisze kod szybko. Ale szybko != poprawnie.
- Live demo: Uzyj Copilota do scaffoldu -> znajdz buga -> napraw go -> wezmij za niego odpowiedzialnosc
- **Jestes odpowiedzialny za kazda linijke.** AI to narzedzie, nie zamiennik.

### Architektura Projektu 1
```
Uzytkownik (przegladarka) -> FastAPI -> LLM (Azure OpenAI)
                                ↓
                          Kod ReportLab (Python string)
                                ↓
                          exec() -> bajty PDF
                                ↓
                          Serwuj PDF + Zapisz embedding w Qdrant
```

### Prompt Engineering do generowania kodu
Kluczowe zasady dla system prompta:
1. Okresl dokladna sygnature funkcji: `create_pdf_content(buffer)`
2. Podaj dokladne importy do uzycia
3. Ostrzez przed czestymi pulapkami ReportLab (ListFlowable, getSampleStyleSheet)
4. Wymagaj strukturyzowanego JSON z polem `code`

### Rozmowa o exec()
- **Na potrzeby tego kursu:** Akceptujemy ryzyko. To twoj laptop, twoj kod.
- **Na produkcji:** To koszmar bezpieczenstwa. Uzywaj strukturyzowanych danych -> szablonow.
- Pokaz `exec_security_demo.py` -- zobacz co moze pojsc nie tak.

---

## Czesc 2 -- Embeddingi, wyszukiwanie wektorowe i myslenie produkcyjne (~2h)

### Utrzymanie to 80% roboty
- Drift promptow: modele sie aktualizuja, twoje prompty przestaja dzialac
- Edge case'y: uzytkownicy cie zaskocza
- Monitoring, logowanie, sledzenie kosztow -- nudne ale niezbedne

### Embeddingi i bazy wektorowe
- **Embedding** = tekst -> gesty wektor ktory oddaje znaczenie
- **Baza wektorowa** = baza danych zoptymalizowana pod "znajdz podobne rzeczy"
- **Qdrant** = uzywamy go in-memory (`QdrantClient(":memory:")`) -- zero Dockera

### Jak dziala Qdrant
```python
# Collection = tabela
# Point = wiersz (wektor + metadane)
# Search = "znajdz K najblizszych wektorow do tego wektora zapytania"
```

### Co embeddowac?
| Strategia | Plusy | Minusy |
|-----------|-------|--------|
| Prompt uzytkownika | Oddaje intencje | Nie obejmuje wygenerowanej tresci |
| Streszczenie outputu | Oddaje tresc | Dodatkowy LLM call |
| Oba polaczone | Najlepsze z obu | Kosztuje wiecej |

---

## Kluczowe wnioski
1. Prompt engineering jest iteracyjny -- spodziewaj sie 10+ poprawek
2. exec() jest potezny ale niebezpieczny -- zawsze omawiaj kompromisy
3. Embeddingi zamieniaja tekst w przeszukiwalne znaczenie
4. Qdrant in-memory jest idealny do prototypowania (na produkcji przejdz na persistent)
