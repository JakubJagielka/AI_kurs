# Lekcja 4 -- Cwiczenia

## Podstawowe

### 1. Dodaj narzedzie do agenta
Otworz `04_agent_with_tools.py` i dodaj nowe narzedzie: `get_random_quote`.
- Ma zwracac losowy inspirujacy cytat z zahardkodowanej listy
- Zdefiniuj schemat narzedzia + funkcje + dodaj do rejestru
- Testuj: "Give me something inspiring and roll a d20"

### 2. Zbuduj konwersacyjnego agenta
Zmodyfikuj `02_agent_loop.py` zeby dzialal w petli przyjmujacej wejscie od uzytkownika:
```
Ty: ktora godzina?
Agent: Jest sroda, 5 marca, 14:32.
Ty: oblicz 42 * 17
Agent: 42 * 17 = 714
Ty: quit
```
Podpowiedz: opakuj wywolanie agenta w petle `while True` z `input()`.

### 3. Zbadaj serwer MCP
Odpal serwer MCP z `03_mcp_server_example/` i podlacz go do VS Code lub Claude Desktop.
- Sprobuj poprosic AI o przeczytanie plikow z twojego projektu
- Sprobuj poprosic o listowanie katalogow
- Co sie dzieje jak poprosisz o przeczytanie pliku ktory nie istnieje?

---

## Zaawansowane

### 4. Stworz wlasny serwer MCP
Zbuduj serwer MCP ktory udostepnia inna funkcjonalnosc:
- **Narzedzie pogodowe** -- zwraca fejkowe/prawdziwe dane pogodowe
- **Narzedzie bazodanowe** -- czyta z bazy SQLite
- **Narzedzie tlumaczace** -- uzywa LLM-a lub biblioteki do tlumaczenia tekstu

Postepuj wedlug wzorca z `03_mcp_server_example/server.py`.

### 5. Agent z pamiecia
Zrob zeby agent pamietal poprzednie rozmowy:
- Przechowuj historie konwersacji w liscie
- Przy kazdym nowym wejsciu uzytkownika dolaczaj pelna historie
- Agent powinien moc odnosic sie do poprzednich odpowiedzi

### 6. Agent odporny na bledy
Dodaj obsluge bledow do petli agenta:
- Co jesli narzedzie rzuci wyjatek? (Zlap go, powiedz LLM-owi co poszlo nie tak)
- Co jesli LLM zahalucynuje nieistniejace narzedzie? (Obsluz to elegancko)
- Dodaj timeout: jesli agent potrzebuje wiecej niz 30 sekund, zatrzymaj go

### 7. Rownolegle wywolania narzedzi
API OpenAI moze zwrocic wiele wywolan narzedzi naraz.
Petla agenta w `02_agent_loop.py` juz to obsluguje.
Testuj: zapytaj o cos co wymaga 2+ narzedzi i zweryfikuj ze oba zostaly wywolane.
