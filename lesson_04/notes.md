# Lekcja 4: Agenci, uzycie narzedzi, MCP i podsumowanie kursu

## Od chatbotow do agentow

### Czym jest agent?
- Chatbot **generuje tekst**
- Agent **podejmuje akcje** -- moze wywolywac funkcje, czytac pliki, odpytywac bazy danych
- Klucz: LLM sam *decyduje* kiedy i ktore narzedzie uzyc

### Petla agenta (wzorzec ReAct)
```
while not done:
    1. OBSERWUJ -- popatrz na aktualny stan / zapytanie uzytkownika
    2. MYSL     -- zdecyduj co robic dalej (rozumowanie LLM-a)
    3. DZIALAJ  -- wywolaj narzedzie albo daj ostateczna odpowiedz
    4. OBSERWUJ -- zobacz wynik narzedzia
    -> powtarzaj az zadanie bedzie ukonczone
```

### Function Calling = fundament
- Definiujesz narzedzia (funkcje) z nazwami, opisami i schematami parametrow
- LLM widzi te definicje i decyduje kiedy ich uzyc
- LLM zwraca strukturyzowana wiadomosc "wywolaj ta funkcje z tymi argumentami"
- TWOJ KOD wykonuje funkcje i odsyla wynik
- LLM formuluje ostateczna odpowiedz uzywajac wyniku narzedzia

---

## Budowanie agentow

### Jedno narzedzie -> wiele narzedzi -> petla agenta
1. `01_function_calling.py` -- Jedno narzedzie (kalkulator). LLM decyduje kiedy uzyc.
2. `02_agent_loop.py` -- Reczna petla agenta w while. Zero frameworkow. Czysty kod.
3. `04_agent_with_tools.py` -- Wiele narzedzi, LLM wybiera odpowiednie.

### Kiedy NIE uzywac agentow
- Proste, deterministyczne zadania -> po prostu napisz normalny kod
- Kiedy potrzebujesz 100% niezawodnosci -> agenci moga halucynowac wywolania narzedzi
- Kiedy liczy sie opoznienie -> kazde wywolanie narzedzia = kolejny round trip do API
- Kiedy liczy sie koszt -> petle agentow moga robic 5-10+ wywolan API na request

---

## MCP -- Model Context Protocol

### Co to jest?
Standardowy protokol dajacy AI dostep do narzedzi i zrodel danych.

### Dlaczego powstal?
Kazda apka AI budowala wlasny system pluginow. MCP = jeden standard zeby rzadzic nimi wszystkimi.

### Architektura
```
Host MCP (Claude Desktop, VS Code, itp.)
    (JSON-RPC przez stdio/SSE)
Serwer MCP (twoje narzedzie -- czytnik plikow, query do bazy, wrapper na API, itp.)
```

### Kluczowe pojecia
- **Tools** -- funkcje ktore AI moze wywolac (jak function calling, ale zestandaryzowane)
- **Resources** -- dane ktore AI moze czytac (pliki, rekordy z bazy itp.)
- **Prompts** -- szablony promptow do ponownego uzycia

---

## Podsumowanie kursu

### Co teraz umiesz
- Cloud LLM API (Azure OpenAI, Gemini, strukturyzowane outputy)
- Prompt engineering do generowania kodu
- Generowanie PDF przez kod generowany przez LLM-a
- Embeddingi i wyszukiwanie wektorowe (Qdrant)
- Lokalna inferencja modeli (Ollama, HuggingFace)
- Modele audio (Whisper STT, TTS)
- Pojecia kwantyzacji
- Agenci AI i function calling
- Podstawy MCP

### Kluczowy przekaz
"Umiem teraz budowac produkty AI" -- a nie "jest tyle czego nie wiem."
Masz fundamenty. Reszta to poglebienie tych samych koncepcji.
