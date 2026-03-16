# Lekcja 2 -- Cwiczenia (cele dodatkowe dla Projektu 1)

## Podstawowe (rob na zajeciach jesli starczy czasu)

### 1. Logika ponownych prob
Kiedy LLM generuje kod ReportLab ktory nie dziala:
- Zlap wyjatek
- Wyslij komunikat bledu z powrotem do LLM-a razem z oryginalnym kodem
- Popros go o naprawienie problemu
- Sprobuj wykonac ponownie (max 3 proby)

To jest prawdziwy produkcyjny wzorzec -- samonaprawiajace sie generowanie kodu.

### 2. Wiele motywow
Dodaj selektor motywu do system prompta. Gdy uzytkownik wybiera:
- **Profesjonalny** -> czyste fonty, paleta niebiesko/szara, formalny layout
- **Kreatywny** -> kolorowy, rozne fonty, dekoracyjne elementy
- **Minimalny** -> duzo bialej przestrzeni, prosta typografia

Dynamicznie modyfikuj system prompt na podstawie wybranego motywu.

### 3. Lepsze wyniki wyszukiwania
Ulepsz endpoint wyszukiwania zeby zwracal:
- Wynik podobienstwa (juz jest)
- Fragment/podglad oryginalnego prompta
- Timestamp wygenerowania PDF-a
- Filtrowanie po minimalnym progu podobienstwa

---

## Zaawansowane

### 4. Pamiec konwersacji
Zachowuj historie czatu zeby uzytkownik mogl mowic:
- "Teraz dodaj spis tresci do tego raportu"
- "Powieksz tytul"
- "Dodaj sekcje o odnawialnej energii"

Bedziesz musial przekazywac poprzednie wiadomosci do wywolania LLM-a.

### 5. Trwaly storage wektorow
Przejdz z `QdrantClient(":memory:")` na `QdrantClient(path="./qdrant_data")`.
Teraz twoje PDF-y przetrwaja restarty serwera. Testuj: generuj PDF-y, zrestartuj serwer, wyszukaj.

### 6. Wyszukiwanie hybrydowe
Polacz podobienstwo wektorowe z filtrowaniem po slowach kluczowych. Przyklad:
- Wyszukiwanie wektorowe znajduje semantycznie podobne PDF-y
- Potem filtruj po zakresie dat lub tagu motywu
- Zwracaj tylko wyniki pasujace do obu kryteriow
