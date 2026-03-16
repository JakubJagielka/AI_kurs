# Praktyczny kurs GenAI Engineering

> **Poziom:** Sredniozaa## Struktura repozytoriumansowany | **Calkowity czas:** 11 godzin (4 bloki lekcyjne) | **Jezyk:** Python  
> **Wymagania wstepne:** Podstawy Pythona, podstawy webu (HTTP, API), umiejetnosc pracy z terminalem  
> **Sprzet:** Dowolny nowoczesny laptop (8GB+ RAM). Nie trzeba GPU (uzywamy API chmurowych + Ollama do lokalnych modeli).

---

## Spis tresci

- [Filozofia kursu](#-filozofia-kursu)
- [Jak dzialaja repozytoria](#-jak-dzialaja-repozytoria)
- [Struktura repozytorium](#-struktura-repozytorium)
- [Stack technologiczny](#-stack-technologiczny)
- [Plany lekcji](#-plany-lekcji)
  - [Lekcja 1: Krajobraz GenAI i opanowanie API (1h)](#lekcja-1-krajobraz-genai-i-opanowanie-api-1h)
  - [Lekcja 2: AI Engineering -- Projekt 1: Generator PDF + Wyszukiwanie semantyczne (4h)](#lekcja-2-ai-engineering--projekt-1-generator-pdf--wyszukiwanie-semantyczne-4h)
  - [Lekcja 3: Swiat open-source -- Hugging Face, lokalne modele i Projekt 2: Generator menu (4h)](#lekcja-3-swiat-open-source--hugging-face-lokalne-modele-i-projekt-2-generator-menu-4h)
  - [Lekcja 4: Agenci, Tool Use, MCP i podsumowanie kursu (2h)](#lekcja-4-agenci-tool-use-mcp-i-podsumowanie-kursu-2h)
- [Podsumowania projektow](#-podsumowania-projektow)
- [Setup i wymagania](#-setup-i-wymagania)
- [Notatki instruktora](#-notatki-instruktora)

---

## Filozofia kursu

To **nie** jest kurs teoretyczny. Studenci buduja **dwa prawdziwe projekty** od poczatku do konca, uczac sie ekosystemu GenAI. Kazdy koncept jest uczony *bo projekt go potrzebuje*, nie abstrakcyjnie.

### Glowne zasady

1. **Napedzane projektami** -- Kazda lekcja posuwa do przodu prawdziwa, dzialajaca aplikacje.
2. **Boilerplate dostarczony** -- Studenci nigdy nie marnuja czasu na CSS, HTML scaffolding, ani routing FastAPI. My to dostarczamy. Oni skupiaja sie na czesciach AI.
3. **Najpierw chmura, potem lokalnie** -- Zaczynamy od API chmurowych (najlatwiejsze, najbardziej niezawodne), potem pokazujemy jak przejsc na open-source/lokalne.
4. **Odpowiedzialnosc inzyniera** -- Uzywamy narzedzi "vibe coding", ale uczymy studentow *byc wlascicielem* i *rozumiec* kazda linijke. AI pisze kod; inzynierowie dostarczaja produkty.
5. **Gotowe do portfolio** -- Kazdy projekt zyje w swoim wlasnym repo na GitHubie studenta. Zadnych klimatow "folder z zadaniami domowymi" -- prawdziwe projekty, prawdziwe repo.

---

## Jak dzialaja repozytoria

Sa **3 oddzielne repozytoria GitHub** do tego kursu:

### 1. Repo kursu (to wlasnie) -- `AI_kurs`
Nalezace do instruktora. Zawiera wszystkie notatki do lekcji, dema, cwiczenia i materialy referencyjne. Studenci **klonuja je do wgladu** ale nie pushuja do niego.

### 2. Szablon Projektu 1 -- `genai-pdf-generator`
**GitHub Template Repository** ktore tworzysz. Zawiera boilerplate FastAPI + HTML z TODO stubami na cala logike AI. Studenci klikaja **"Use this template"** na GitHubie zeby stworzyc wlasna kopie (np. `github.com/student-name/genai-pdf-generator`). Pracuja nad nim podczas lekcji 2. To **ich repo**, z **ich commitami**, na **ich profilu GitHub**.

### 3. Szablon Projektu 2 -- `genai-menu-generator`
Ten sam wzorzec. Template repo z boilerplate. Studenci tworza wlasna kopie do lekcji 3.

**Workflow studenta:**
```
1. github.com/instructor/genai-pdf-generator -> "Use this template" -> github.com/student/genai-pdf-generator
2. git clone -> praca na zajeciach -> git commit -> git push
3. Powtorz dla Projektu 2
```

**Rezultat:** Kazdy student wychodzi z **2 repo gotowymi do portfolio** na wlasnym GitHubie z wlasna historia commitow. Bez zasmiecania folderami kursowymi.

---

## 📁 Repository Structure

### To repo -- `AI_kurs/`

```
AI_kurs/
├── README.md                          # Ten plik -- pelny plan kursu
│
├── lesson_01/
│   ├── notes.md                       # Notatki instruktora i tresc slajdow
│   ├── demos/
│   │   ├── 01_first_llm_call.py       # Proste wywolanie Azure OpenAI / Gemini
│   │   ├── 02_vision_api.py           # Wysylanie obrazu do modelu multimodalnego
│   │   ├── 03_image_generation.py     # Generowanie obrazu przez DALL-E
│   │   ├── 04_embeddings_intro.py     # Generowanie embeddingu, pokaz wektora
│   │   ├── 05_api_config_patterns.py  # Zmienne srodowiskowe, retry, timeouty, wybor modelu
│   │   ├── 06_function_calling_intro.py # Function calling -- daj LLM narzedzie
│   │   ├── 07_web_search_grounding.py # Grounded search -- LLM + dane w czasie rzeczywistym
│   │   ├── 08_chat_with_memory.py      # Zaawansowane: Czat z pamięcią konwersacji
│   │   ├── 09_multi_provider_compare.py # Zaawansowane: Ten sam prompt -> Azure OpenAI vs Gemini
│   │   └── 10_structured_json_output.py # Structured output -- LLM zwraca JSON z gwarantowanym schematem
│   └── exercises.md                   # Cwiczenia podstawowe + zaawansowane
│
├── lesson_02/
│   ├── notes.md                       # AI mindset, planowanie, vibe coding, utrzymanie, teoria embeddingov
│   ├── demos/
│   │   ├── cosine_similarity_demo.py  # Pokaz podobienstwa miedzy zdaniami
│   │   └── exec_security_demo.py      # Dlaczego exec() jest niebezpieczne (lekcja)
│   └── exercises.md                   # Cele rozszerzajace do Projektu 1
│
├── lesson_03/
│   ├── notes.md                       # HuggingFace, koncepcje PyTorch, kwantyzacja, lokalne AI
│   ├── demos/
│   │   ├── 01_huggingface_pipeline.py # pipeline() do analizy sentymentu/klasyfikacji
│   │   ├── 02_whisper_stt.py          # Speech-to-Text z Whisper
│   │   ├── 03_tts_demo.py            # Demo Text-to-Speech
│   │   ├── 04_ollama_intro.py         # Wywolanie lokalnego LLM przez Ollama
│   │   └── sample_audio/
│   │       └── test_clip.wav          # Audio do demo STT
│   ├── exercises.md                   # Cele rozszerzajace do Projektu 2
│   └── resources/
│       └── model_cheatsheet.md        # Sciaga: modele do kazdego zadania + rozmiary
│
├── lesson_04/
│   ├── notes.md                       # Teoria agentow, function calling, MCP
│   ├── demos/
│   │   ├── 01_function_calling.py     # Azure OpenAI function calling -- kalkulator
│   │   ├── 02_agent_loop.py           # Prosta petla agenta w stylu ReAct (bez frameworka)
│   │   ├── 03_mcp_server_example/     # Minimalny serwer MCP
│   │   │   ├── server.py
│   │   │   └── README.md
│   │   └── 04_agent_with_tools.py     # Agent z wieloma narzedziami
│   ├── exercises.md                   # "Dodaj narzedzie do agenta", "Stworz serwer MCP"
│   └── resources/
│       └── whats_next.md              # Wyselekcjonowane sciezki nauki
│
└── resources/
    └── setup_guide.md                 # Instrukcja konfiguracji przed kursem
```

### Szablon Projektu 1 -- `genai-pdf-generator/`

```
genai-pdf-generator/
├── app/
│   ├── main.py                # Aplikacja FastAPI -- routy gotowe, logika AI = TODO
│   ├── llm_service.py         # TODO: Wywolanie LLM + prompt engineering na kod ReportLab
│   ├── pdf_generator.py       # TODO: Wykonaj kod ReportLab wygenerowany przez LLM -> bajty PDF
│   ├── embedding_service.py   # TODO: Generuj embeddingi dla wygenerowanych PDF-ow
│   ├── vector_store.py        # TODO: Integracja z Qdrant -- zapis + wyszukiwanie embeddingov
│   └── schemas.py             # Modele Pydantic (czesciowo dostarczone)
├── static/
│   ├── index.html             # UI czatu + przegladarka PDF + panel wyszukiwania (gotowe)
│   ├── style.css              # Dostarczony
│   └── app.js                 # Frontend JS -- wszystkie fetch calls (dostarczony)
├── output/                    # Wygenerowane PDF-y laduja tutaj (.gitkeep)
├── requirements.txt           # fastapi, uvicorn, openai, reportlab, qdrant-client, numpy
├── .env.example               # AZURE_OPENAI_API_KEY=..., AZURE_OPENAI_ENDPOINT=..., GEMINI_API_KEY=...
├── .gitignore
└── README.md                  # Opis projektu, konfiguracja, co zaimplementowac
```

### Szablon Projektu 2 -- `genai-menu-generator/`

```
genai-menu-generator/
├── app/
│   ├── main.py                # Aplikacja FastAPI -- routy generowania menu (stuby)
│   ├── llm_local.py           # TODO: Generowanie tekstu menu przez Ollama
│   ├── image_generator.py     # TODO: Generowanie obrazow (DALL-E lub lokalne)
│   └── schemas.py             # Modele Pydantic dla pozycji menu
├── static/
│   ├── index.html             # UI wyswietlania menu -- siatka kart z obrazami (dostarczony)
│   ├── style.css              # Dostarczony
│   └── app.js                 # Dostarczony
├── output/                    # Wygenerowane obrazy menu (.gitkeep)
├── requirements.txt           # fastapi, uvicorn, ollama, openai, Pillow
├── .env.example               # AZURE_OPENAI_API_KEY=..., GEMINI_API_KEY=..., OLLAMA_BASE_URL=...
├── .gitignore
└── README.md                  # Opis projektu, konfiguracja, co zaimplementowac
```

---

## Stos technologiczny

| Kategoria | Narzedzie | Dlaczego |
|-----------|-----------|----------|
| **Jezyk** | Python 3.11+ | Standard w branzy AI/ML |
| **Backend** | FastAPI | Lekki, asynchroniczny, swietny do API |
| **Frontend** | Czysty HTML/CSS/JS | Zero builda, zero komplikacji frontendowych |
| **Cloud LLM** | Azure OpenAI (glowny), Gemini (alternatywa) | Klasa enterprise, wsparcie structured output |
| **Lokalny LLM** | Ollama | Odpala skwantyzowane modele na CPU, proste API, bez GPU |
| **Generowanie PDF** | ReportLab (przez kod Python generowany przez LLM + `exec()`) | Najpotezniejsza biblioteka PDF w Pythonie |
| **Embeddingi** | Azure OpenAI `text-embedding-3-small` | Tanie, szybkie, swietna jakosc |
| **Baza wektorowa** | Qdrant (in-memory przez klienta Python) | Proste, bez Dockera, `pip install qdrant-client` |
| **Audio** | HuggingFace Transformers (Whisper, TTS) | Standard w branzy, dobre male modele |
| **Generowanie obrazow** | DALL-E API (glowny), Stable Diffusion (tylko demo) | Niezawodne do projektu |
| **Narzedzia dev** | VS Code + GitHub Copilot | Praktykujemy to czego uczymy |

---

## Plany lekcji

---

### Lekcja 1: Krajobraz GenAI i opanowanie API (1h)

> **Cel:** Studenci wychodza rozumiejac ekosystem GenAI, po pierwszych wywolaniach API, I po zobaczeniu prawdziwych wzorcow inzynierskich (function calling, konfiguracje, web search) ktore odrozniaja zabawkowe skrypty od kodu produkcyjnego.

#### Tematy

**Krajobraz (~15min)**
- Czym sa LLM-y, modele embeddingowe i generatory obrazow?
- Dostawcy chmurowi: Azure OpenAI, Google Gemini i alternatywy open-source
- Jak to dziala na wysokim poziomie: tokeny, okna kontekstowe, temperature, system prompty
- Szybkie "jak dzialaja Transformery" -- wejscie -> tokeny -> attention -> wyjscie. 60 sekund, bez matmy. Tyle zeby odczarowac temat.

**Dema podstawowe + kodowanie z instruktorem (~20min)**
- `01_first_llm_call.py` -- Generowanie tekstu z Azure OpenAI. Zmien prompt, model, temperature. Zobacz co sie stanie.
- `02_vision_api.py` -- Wyslij obraz do modelu multimodalnego, dostaniesz opis.
- `03_image_generation.py` -- Wygeneruj obraz z prompta tekstowego przez DALL-E.
- `04_embeddings_intro.py` -- Wygeneruj wektor embeddingu, wyswietl go, wytlumacz co reprezentuje. "Tak komputery rozumieja znaczenie."

**Poza Hello World -- prawdziwe wzorce API (~20min)**
- `05_api_config_patterns.py` -- Pokaz jak profesjonalisci konfiguruja klientow LLM: zmienne srodowiskowe, logika retry, obsluga timeoutow, dynamiczny wybor modeli. Nie tylko zahardkodowane `openai.chat.completions.create()`.
- `06_function_calling_intro.py` -- **Zapowiedz Function Calling**: Daj LLM-owi narzedzie `get_weather`. Pokaz ze *decyduje sie* wywolac funkcje zamiast zmyslac dane pogodowe. "Tak dzialaja pluginy ChatGPT. Tak dzialaja agenty. Swojego zbudujemy w Lekcji 4."
- `07_web_search_grounding.py` -- Pokaz wywolanie grounded search (Azure OpenAI z web search, albo API w stylu Perplexity). "LLM-y nie znaja dzisiejszych wiadomosci. Ale mozesz im dac narzedzia ktore znaja." Dyskusja: kiedy groundowac wyszukiwaniem vs. kiedy zaufac wiedzy modelu.
- `10_structured_json_output.py` -- **Structured Output**: LLM zwraca JSON z gwarantowanym schematem. Pokaz dwa podejscia: `response_format=json_object` (prosty ale bez gwarancji schematu) i `json_schema` (strict mode -- LLM MUSI zwrocic dokladna strukture). Praktyczny przyklad: ekstrakcja danych kontaktowych z chaotycznego tekstu. "Tak laczycie LLM-y z reszta kodu -- przez ustrukturyzowane dane, nie parsowanie stringow."

> **Zaawansowane/Opcjonalne** -- Dla szybkich studentow albo jako demo jesli starczy czasu:
> - `08_chat_with_memory.py` -- Czat z pamięcią konwersacji. LLM nie ma wbudowanej pamieci -- to MY wysylamy cala historie wiadomosci za kazdym razem. Studenci rozmawiaja z botem, podaja imie, potem pytaja "jak mam na imie?" -- i dziala. Na koniec pokaz rosnaca liste messages. "Dlatego dlugie konwersacje kosztuja wiecej."
> - `09_multi_provider_comparison.py` -- Ten sam prompt wyslany do Azure OpenAI i Gemini. Porownaj jakosc odpowiedzi, szybkosc i koszt. "Nie ma jednego najlepszego modelu. Zalezy od zadania."

**Podsumowanie (~5min)**
- Praca domowa: Odpal wszystkie podstawowe dema. Sprobuj zaawansowanych jesli jestes ciekawy. Zainstaluj Ollama (przyda sie pozniej).
- Zapowiedz nastepnej lekcji: "Teraz znasz narzedzia. Nastepnym razem budujemy prawdziwy produkt."

#### Notatki instruktora
- Ta lekcja to **haczyk** ale tez ustawia poprzeczke. Studenci powinni wyjsc z poczuciem "to wiecej niz sie spodziewalem" a nie "to moglem wyguglowac."
- Demo function calling to **celowe foreshadowing** Lekcji 4 (Agenty). Posiej ziarno wczesnie.
- Web search grounding pokazuje ograniczenia LLM-ow *i* rozwiazanie w jednym demie. Mocny moment edukacyjny.
- **Kazdy student musi wyjsc z dzialajacym kluczem API** bo inaczej utknie na nastepnych zajeciach. Miej 1-2 zapasowe klucze z limitami wydatkow.

---

### Lekcja 2: AI Engineering -- Projekt 1: Generator PDF + Wyszukiwanie Semantyczne (4h)

> **Cel:** Studenci buduja kompletna aplikacje webowa: Czat -> LLM generuje kod ReportLab -> piekny PDF. Potem dodaja wyszukiwanie semantyczne po wszystkich wygenerowanych PDF-ach uzywajac embeddingov i Qdrant. To jeden ciagy projekt na ~4 godziny (dwie sesje po 2h, albo jedna dluga z przerwa).

#### Czesc 1 -- AI Mindset i podstawowe generowanie PDF (~2h)

**AI Engineering Mindset (Wyklad + Dyskusja)**
- Dlaczego uzywac AI? Dlaczego automatyzowac? Jakie problemy biznesowe pasuja do LLM-ow -- a jakie *nie dzialaja*?
- Jak podejsc do projektu AI jako inzynier: zidentyfikuj zadanie, wybierz odpowiednie narzedzie, zaplanuj architekture
- Jak rozmawiac z interesariuszami o mozliwosciach i ograniczeniach AI
- Wybor stosu: API vs. lokalne, framework vs. raw, kiedy czego uzywac

**Vibe Coding i odpowiedzialnosc**
- Demo na zywo: Uzyj Copilota/Cursora do szybkiego scaffoldowania
- Potem pokaz buga ktory wprowadzil. Przejdz przez niego. Napraw.
- Kluczowy przekaz: "AI pisze kod. Ty shipujesz produkty. Ty jestes odpowiedzialny za kazda linijke."

**Setup Projektu 1**
- Studenci tworza wlasne repo z szablonu `genai-pdf-generator` na GitHubie
- Klonowanie, instalacja deps (`pip install -r requirements.txt`), odpalenie apki (`uvicorn app.main:app --reload`)
- Zwiedzanie boilerplate'u: "Tu jest UI (nie ruszac), tu sa routy (gotowe), tu sa TODO (wasza robota)"

**Implementacja: LLM -> kod ReportLab**
- `llm_service.py`: Serce projektu -- napisz system prompt ktory instruuje LLM zeby generowal funkcje `create_pdf_content(buffer)` uzywajac ReportLab
- Ucz prompt engineeringu: dlaczego system prompt potrzebuje konkretnych regul o `getSampleStyleSheet()`, pulapkach `ListFlowable`, wymaganiach importow itd.
- LLM zwraca JSON z polem `code` (structured output przez response format)
- Test: Wyslij request, zbadaj wygenerowany kod Python. Czy wyglada dobrze?

**Implementacja: exec() -> PDF**
- `pdf_generator.py`: Wez wygenerowany string z kodem, przygotuj srodowisko wykonania (bezpieczne importy: `reportlab`, `io`, `colors` itd.), `exec()`, wywolaj `create_pdf_content(buffer)`, zwroc bajty PDF
- **Moment edukacyjny -- rozmowa o exec():**
  - "To dziala. To robi wrazenie. Ale wykonujemy arbitralny kod wygenerowany przez LLM."
  - "Na twoim laptopie do cwiczen? Okej. Na produkcji z inputem uzytkownika? **Katastrofa.**"
  - Pokaz `exec_security_demo.py` -- zlosliwy string z kodem ktory czyta pliki / odpala komendy shell
  - Dyskusja: Jak zrobilbys to bezpieczniej? (Sandboxing, restricted exec, alternatywa oparta na structured data)
  - "Na ten kurs akceptujemy ryzyko. W pracy uzylbys structured JSON -> generowanie na podstawie szablonow."

**Integracja i testowanie**
- Polacz wszystko end-to-end: Uzytkownik pisze na czacie -> LLM generuje kod ReportLab -> exec -> PDF wyswietlony w przegladarce
- Testuj roznymi promptami: "Stworz profesjonalny raport o zmianach klimatu", "Zrob zabawne zaproszenie na imprezke"
- Zobacz co sie psuje. Debugujcie razem. Tu sie odbywa prawdziwa nauka.

> **Zaawansowane/Opcjonalne** -- Dla szybkich studentow:
> - Dodaj **logike retry**: Jesli wygenerowany kod sie nie kompiluje, zlap wyjatek, wyslij blad z powrotem do LLM-a i popros o naprawe. Automatyczne samonaprawianie.
> - Dodaj **wybor motywu**: Niech uzytkownicy wybieraja motyw wizualny (Profesjonalny, Swobodny, Imprezowy) ktory modyfikuje system prompt i produkuje rozne style ReportLab.
> - Dodaj **pamiec konwersacji**: Trzymaj historie czatu zeby uzytkownik mogl powiedziec "teraz dodaj tabelke do tego raportu" a LLM pamietalby poprzedni PDF.

#### Czesc 2 -- Embeddingi, wyszukiwanie wektorowe i myslenie produkcyjne (~2h)

**Trudna czesc: Utrzymanie**
- "Twoje demo dziala. I co dalej?"
- Prompt drift: modele sa aktualizowane, twoje prompty sie psuja
- Edge case'y: uzytkownicy wpisza rzeczy ktorych nigdy sobie nie wyobraziles
- Ryzyko exec() rosnie w czasie gdy wiecej ludzi uzywa apki
- Monitoring, logowanie, sledzenie kosztow -- nudne ale niezbedne
- Kluczowy przekaz: Zbudowanie MVP to 20% roboty. Utrzymanie to 80%.

**Embeddingi i bazy wektorowe**
- Czym jest embedding? Tekst -> gesty wektor ktory oddaje *znaczenie*
- Demo na zywo: `cosine_similarity_demo.py` -- osadz "szczesliwy pies" i "radosny szczeniak" vs "fizyka kwantowa". Pokaz liczby.
- Czym jest baza wektorowa? To baza danych zoptymalizowana pod "znajdz mi rzeczy *podobne* do tego"
- Dlaczego nie zwykly PostgreSQL? (Mozna, ale bazy wektorowe sa zoptymalizowane pod wyszukiwanie podobienstwa na skale)
- Qdrant: Uzywamy **in-memory** przez klienta Python -- bez Dockera, bez serwera, po prostu `pip install qdrant-client` i `QdrantClient(":memory:")`
- Wytlumacz: kolekcje, punkty (wektor + payload), wyszukiwanie podobienstwa

**Implementacja: Serwis embeddingowy**
- `embedding_service.py`: Po kazdym wygenerowanym PDF-ie stworz embedding zawartosci
- Co osadzac? Dyskusja o kompromisach:
  - Prompt uzytkownika? (Oddaje intencje)
  - Podsumowanie wygenerowanej tresci? (Oddaje output)
  - Oba polaczone? (Najlepsze z dwoch swiatow, kosztuje wiecej)
- Zapis: wektor embeddingu + metadane (tytul, nazwa pliku, timestamp, oryginalny prompt) jako punkt Qdrant

**Implementacja: Wyszukiwanie semantyczne**
- `vector_store.py`: Nowy endpoint `/search`
- Osadz zapytanie uzytkownika -> znajdz top-K najblizszych sasiadow w Qdrant -> zwroc wyniki z wynikami podobienstwa
- UI juz ma gotowy panel wyszukiwania (boilerplate) -- potrzebuje tylko dzialajacego API
- Test: Wygeneruj 5+ roznych PDF-ow, potem wyszukuj. "Znajdz mi cos o nauce" powinno pasowac do raportu klimatycznego nawet jesli nigdy nie uzyles slowa "nauka" w prompcie.

> **Zaawansowane/Opcjonalne** -- Dla szybkich studentow:
> - Dodaj **filtrowanie metadanych**: Filtruj wyniki po zakresie dat lub motywie, nie tylko podobienstwo wektorowe.
> - Dodaj **prog podobienstwa**: Zwracaj tylko wyniki powyzej okreslonego progu. Dyskusja: jaki prog jest dobry? (Spoiler: to zalezy.)
> - Sprobuj **roznych strategii embeddingu**: Osadz sam prompt vs. prompt + podsumowanie wygenerowanego PDF. Porownaj jakosc wyszukiwania.
> - Uzyj **trwalego zapisu Qdrant**: `QdrantClient(path="./qdrant_data")` zeby PDF-y przetrwaly restart serwera.

**Podsumowanie i retrospektywa**
- Pelne demo kompletnej apki: Czat -> Generuj PDF -> Wyszukuj poprzednie PDF-y po znaczeniu
- Czego sie nauczylismy? Co bylo trudniejsze niz sie spodziewalismy?
- Studenci commituja i pushuja swoja prace
- Zapowiedz: "Do tej pory placilismy za API chmurowe za wszystko. Nastepnym razem -- a co gdybysmy nie musieli?"

#### Kluczowe pliki (w repo szablonu `genai-pdf-generator`)
- `app/llm_service.py` -- **Glowna praca studenta**: prompt LLM + structured output na kod ReportLab
- `app/pdf_generator.py` -- **Praca studenta**: wykonanie exec() + generowanie bajtow PDF
- `app/embedding_service.py` -- **Praca studenta**: Generowanie embeddingov + zapis do Qdrant
- `app/vector_store.py` -- **Praca studenta**: Logika wyszukiwania semantycznego
- `app/schemas.py` -- Modele Pydantic (czesciowo dostarczone, studenci rozszerzaja)

#### Krytyczne punkty dydaktyczne
- **Dyskusja o exec() jest niezbedna.** Nie pomijaj jej. To najbardziej zapamietywany moment kursu i uczy prawdziwego zagrozenia produkcyjnego.
- **Qdrant in-memory to jedyne podejscie.** Bez Dockera. `QdrantClient(":memory:")` dziala wszedzie. Wada: dane tracone po restarcie. Na kurs to okej. Wspomnij o trwalym zapisie na dysk (`QdrantClient(path="./qdrant_data")`) jako nastepny krok.
- Moment "aha" wyszukiwania semantycznego -- kiedy zapytanie znajduje pasujacy PDF uzywajac kompletnie innych slow -- jest potezny. Upewnij sie ze studenci wygeneruja dość roznych PDF-ow zeby to zobaczyc.
- Jesli brakuje czasu, funkcja embeddingov/wyszukiwania jest czescia do wyciecia. Podstawowe generowanie PDF to priorytet.

---

### Lekcja 3: Swiat open-source -- Hugging Face, lokalne modele i Projekt 2: Generator menu (4h)

> **Cel:** Studenci uciekaja z chmury. Ucza sie nawigowac HuggingFace, odpalac modele lokalnie z Ollama i Transformers, rozumiec kwantyzacje na poziomie koncepcyjnym i buduja Projekt 2 -- generator menu AI uzywajacy lokalnych LLM-ow + generowania obrazow.

#### Czesc 1 -- Hugging Face, lokalne modele i teoria (~2h)

**Ekosystem HuggingFace**
- HuggingFace Hub: Modele, Datasety, Spaces -- "GitHub dla modeli AI"
- Jak czytac Model Card: Na co patrzec -- architektura, liczba parametrow, licencja, benchmarki, zamierzone uzycie, ograniczenia
- Przejscie na zywo: Znajdz model do analizy sentymentu. Przeczytaj jego karte. Oces czy pasuje do twojego zastosowania.
- Biblioteka `transformers`: `pipeline()` jako najprostszy punkt wejscia
- Demo: `01_huggingface_pipeline.py` -- analiza sentymentu w 3 linijkach kodu
- Kluczowe rozroznienie: `pipeline()` jest swietne do **malych, wyspecjalizowanych modeli** (sentyment, NER, klasyfikacja). Nie probuj ladowac 7B LLM-a w ten sposob na laptopie.

**Ollama: Lokalne LLM-y po prostu**
- Czym jest Ollama? Narzedzie ktore odpala skwantyzowane LLM-y lokalnie z prostym API
- Dlaczego nie czysty `transformers` do LLM-ow? (Zarzadzanie pamiecia, kwantyzacja, predkosc -- Ollama ogarnia to wszystko)
- Demo: `04_ollama_intro.py` -- ten sam wzorzec API co Azure OpenAI, ale wszystko dziala na twojej maszynie
- Porownaj: Odpowiedz API chmurowego vs. odpowiedz Ollama. Dyskusja o predkosci, jakosci, koszcie, prywatnosci.
- Studenci weryfikuja ze ich Ollama dziala z malym modelem (`llama3.2:3b` albo `qwen2.5:3b`)

**Modele audio: STT i TTS**
- Speech-to-Text: Whisper (model OpenAI, ale dziala lokalnie przez `transformers`)
- Demo: `02_whisper_stt.py` -- transkrypcja `test_clip.wav`
- Text-to-Speech: Demo malego modelu TTS
- Demo: `03_tts_demo.py` -- generuj mowe z tekstu
- Studenci probuja: Nagraj krotki klip, transkrybuj go. Fajne i zapamietywalne.

**Pod maska: PyTorch i kwantyzacja**
- Czym jest PyTorch? Biblioteka tensorow -> framework sieci neuronowych -> silnik pod wszystkim czego uzywalismy
- Co sie dzieje kiedy wywolujesz `model.generate()`? Tokenizacja -> forward pass -> sampling -> detokenizacja
- Pokaz pare linii czystego PyTorch -- `torch.tensor`, ksztalty, dtypy -- odczaruj, nie ucz
- Kluczowe liczby: "7B parametrow" = ~14 GB w FP16. Dlatego twoj laptop nie zaladuje tego na surowo.
- **Kwantyzacja**: Zmniejsz precyzje (FP16 -> INT8 -> INT4). Wieksza kompresja = mniejszy + szybszy, ale troche nizsza jakosc.
- Format GGUF: Czym jest, dlaczego Ollama go uzywa. "Kiedy pullowales `llama3.2:3b`, dostalas skwantyzowany model GGUF."
- **Fine-tuning (tylko teoria)**: LoRA, QLoRA -- co robia, kiedy bys ich uzyl. "Potrzebujesz GPU i godzin treningu. Nie robimy tego dzisiaj, ale powinienes wiedziec ze istnieje."
- Kluczowy przekaz: **Nie musisz fine-tunowac w 90% przypadkow.** Dobry prompting + RAG daje ci bardzo wiele.

**Kiedy czego uzywac: Ramka decyzyjna**
- API chmurowe: Najlepsza jakosc, najlatwiejsze, kosztuje, dane opuszczaja twoja maszyne
- Ollama/lokalne LLM-y: Darmowe, prywatne, "wystarczajaco dobre" do wielu zadan, ograniczone przez hardware
- Wyspecjalizowane modele HuggingFace: Najlepsze do konkretnych zadan (STT, NER, klasyfikacja)
- Hybrydowe: Chmura do generowania, lokalnie embeddingi, HF do audio. Mieszaj i dopasowuj.

#### Czesc 2 -- Projekt 2: Generator menu (~2h)

**Setup Projektu 2**
- Studenci tworza wlasne repo z szablonu `genai-menu-generator`
- Klonowanie, instalacja deps, odpalenie apki
- Zwiedzanie boilerplate'u: Backend FastAPI ze stubami, UI oparty na kartach do wyswietlania pozycji menu

**Implementacja: Generowanie tekstu menu z Ollama**
- `llm_local.py`: Wywolanie API Ollama z kreatywnym system promptem
- Input: motyw/kuchnia restauracji (np. "podwodna japońska fuzja")
- Output: ustrukturyzowane pozycje menu -- nazwa, opis, cena (tryb JSON w Ollama)
- Wzmocnij wzorzec structured output z Projektu 1 -- ta sama zasada, inne narzedzie
- Testuj roznymi motywami. Oceniaj jakosc outputu. Probuj roznych modeli.
- Studenci ktorzy chca uzyc API chmurowego (np. nie mogli zainstalowac Ollama) -- w porzadku, wzorzec kodu jest ten sam.

**Implementacja: Generowanie obrazow**
- `image_generator.py`: Dla kazdej pozycji menu wygeneruj obraz jedzenia
- **Glowna sciezka**: DALL-E API -- niezawodne, szybkie, swietne obrazy jedzenia
- **Pokaz (tylko demo)**: HuggingFace `diffusers` / Stable Diffusion. Wytlumacz koncept, ale zaznacz ze na CPU jest za wolne do faktycznego projektu.
- Kazda karta pozycji menu dostaje: nazwe, opis, cene i wygenerowany obraz jedzenia

**Integracja i demo**
- Pelny flow: Wybierz motyw -> Generuj pozycje menu -> Generuj obrazy -> Wyswietl piekne karty menu
- Studenci robia screenshoty swoich menu -- to jest moment "wow". Fajne, wizualne, do pokazania.
- Testuj edge case'y: dziwne motywy, dlugie nazwy, diety specjalne

**Podsumowanie**
- Studenci commituja i pushuja swoja prace
- Oba projekty portfolio sa teraz gotowe!
- Zapowiedz Lekcji 4: "A co gdyby LLM mogl *robic rzeczy*? Nie tylko generowac tekst, ale przeszukiwac web, czytac pliki, odpytywac bazy danych?"

#### Kluczowe pliki (w repo szablonu `genai-menu-generator`)
- `app/llm_local.py` -- **Glowna praca studenta**: Integracja Ollama + strukturalne generowanie menu
- `app/image_generator.py` -- **Praca studenta**: Generowanie obrazow do pozycji menu
- `app/schemas.py` -- Modele Pydantic dla pozycji menu

#### Krytyczne punkty dydaktyczne
- **Miej modele Ollama sciagniete wczesniej.** Pierwsze pulle to 1-3 GB i zablokuja wifi sali. Powiedz studentom zeby zainstalowali + pullowali przed zajeciami. Miej plan B (API chmurowe).
- **Nie pozwol studentom ladowac modelu 7B w czystym `transformers`.** Crashnie. Od tego jest Ollama.
- Kwantyzacja to **teoria + wyjasnienie Ollama**, nie praktyczna kwantyzacja.
- Fine-tuning to **scisle teoria**. Posiej ziarno, daj zasoby do samodzielnej nauki.
- Generowanie obrazow to moment "wow" -- upewnij sie ze dziala niezawodnie. DALL-E jako glowne.

---

### Lekcja 4: Agenty, uzycie narzedzi, MCP i podsumowanie kursu (2h)

> **Cel:** Studenci rozumieja jak dzialaja agenty AI, widza function calling w akcji, poznaja MCP i wychodza z jasnym obrazem co dalej.

**Dokonczenie Projektu 2 (jesli potrzeba)**
- Czas buforowy dla tych co nie skonczyli generowania obrazow
- Finalne demo ich generatorow menu

**Od chatbotow do agentow**
- Czym jest "agent"? LLM ktory moze **podejmowac akcje**, nie tylko generowac tekst
- Kluczowa innowacja: Function Calling / Tool Use -- LLM moze *zdecydowac* zeby uzyc narzedzia
- Demo `01_function_calling.py`: Daj Azure OpenAI narzedzie kalkulator. Zapytaj "ile jest 1547 * 382?" -- patrz jak LLM wywoluje kalkulator zamiast zgadywac.
- Petla agenta: Obserwuj -> Mysl -> Dzialaj -> Obserwuj -> Mysl -> Dzialaj... (wzorzec ReAct)
- Demo `02_agent_loop.py`: Reczna petla agenta (bez frameworka). Petla while + dispatch narzedzi. Studenci widza faktyczna logike.

**Budowanie agenta z wieloma narzedziami**
- Demo `04_agent_with_tools.py`: Agent z wieloma narzedziami (kalkulator, stub web search, czytnik plikow)
- Przejdz przez kod: Jak definiuje sie narzedzia, jak LLM wybiera jedno, jak wyniki wracaja
- **Cwiczenie dla studentow**: Dodaj nowe narzedzie do agenta (z prowadzeniem -- np. narzedzie "aktualny czas")
- Dyskusja o ograniczeniach: Koszt (kazde wywolanie narzedzia = wiecej wywolan API), opoznienia, niezawodnosc, halucynowane wywolania narzedzi
- Kiedy uzywac agentow vs. prostych deterministycznych pipeline'ow

**MCP -- Model Context Protocol**
- Czym jest MCP? Standardowy protokol do dawania AI dostepu do narzedzi i danych
- Dlaczego istnieje? Kazde narzedzie AI budowalo wlasny system pluginow -> potrzeba standardu
- Architektura: MCP Host (Claude Desktop, VS Code itp.) <-> MCP Server (twoje narzedzie)
- Demo `03_mcp_server_example/`: Minimalny serwer MCP ktory udostepnia narzedzie do czytania plikow
- Pokaz podlaczenie go do Claude Desktop albo VS Code
- Zastosowania w realu: Dostep do bazy danych, wewnetrzne narzedzia firmowe, systemy plikow, API

**Podsumowanie kursu i nastepne kroki**
- Rekapitulacja: Co zbudowalismy przez 4 lekcje i 2 projekty
- Inwentarz umiejetnosci -- studenci teraz wiedza:
  - Integracja z API chmurowych LLM-ow (Azure OpenAI, Gemini, structured outputs)
  - Prompt engineering do generowania kodu
  - Generowanie PDF przez kod wygenerowany przez LLM
  - Embeddingi i wyszukiwanie wektorowe (Qdrant)
  - Lokalna inferencja modeli (Ollama, HuggingFace Transformers)
  - Modele audio (Whisper STT, TTS)
  - Koncepcje kwantyzacji
  - Agenty AI i function calling
  - Podstawy MCP
- Co dalej:
  - **Glebszy AI Engineering**: LangChain, LlamaIndex, CrewAI, bardziej zlozone architektury agentow
  - **ML Engineering**: MLOps, deployment modeli, monitoring, ewaluacja
  - **Specjalizacja**: Fine-tuning (z GPU), computer vision, pipeline'y audio
  - **Produkty**: Budowanie SaaS z funkcjami AI, narzedzia wewnetrzne, automatyzacje
- Zasoby: `whats_next.md` ma wyselekcjonowane linki do kazdej sciezki
- Pytania i feedback

#### Kluczowe pliki
- `lesson_04/demos/01_function_calling.py` -- Function calling z jednym narzedziem
- `lesson_04/demos/02_agent_loop.py` -- Reczny agent ReAct (bez frameworka)
- `lesson_04/demos/03_mcp_server_example/` -- Serwer MCP + instrukcje polaczenia
- `lesson_04/demos/04_agent_with_tools.py` -- Agent z wieloma narzedziami
- `lesson_04/resources/whats_next.md` -- Wyselekcjonowane sciezki nauki

#### Krytyczne punkty dydaktyczne
- **Najpierw zbuduj petle agenta recznie** (bez LangChain). Studenci musza zobaczyc ze to po prostu petla while z ifami zanim uzyja jakiegokolwiek frameworka.
- MCP jest nowe dla wiekszosci ludzi. Poswiec czas na *dlaczego* istnieje zanim pokazesz *jak*.
- Podsumowanie powinno byc **motywujace, nie przytlaczajace**. "Moge budowac produkty AI" -- a nie "jest tyle czego nie wiem."

---

## Podsumowania projektow

### Projekt 1: Generator PDF z AI + wyszukiwanie semantyczne

**Repo:** `genai-pdf-generator` (szablon GitHub -> wlasne repo studenta)

**Co studenci buduja:** Aplikacja webowa gdzie uzytkownicy opisuja dokument w interfejsie czatu, chmurowy LLM generuje kod Python ReportLab, backend wykonuje go tworzac piekny tematyczny PDF, a uzytkownicy moga semantycznie wyszukiwac wszystkie wczesniej wygenerowane PDF-y po znaczeniu.

**Cwiczone umiejetnosci:** Integracja z API chmurowych LLM-ow, prompt engineering do generowania kodu, structured outputs, wykonywanie kodu przez exec() (+ dyskusja o bezpieczenstwie), embeddingi, bazy wektorowe (Qdrant in-memory), wyszukiwanie semantyczne, FastAPI.

**Kluczowy wzorzec:** LLM -> structured output (JSON z kodem) -> exec() -> bajty PDF. Plus dyskusja dlaczego to jest potezne ale niebezpieczne, i jak wyglada alternatywa bezpieczna produkcyjnie.

### Projekt 2: Generator menu z AI

**Repo:** `genai-menu-generator` (szablon GitHub -> wlasne repo studenta)

**Co studenci buduja:** Aplikacja webowa gdzie uzytkownicy wybieraja motyw restauracji, **lokalny** LLM (przez Ollama) generuje kreatywne pozycje menu ze structured output, a generator obrazow tworzy zdjecia kazdego dania -- wyswietlane jako wizualna siatka kart menu.

**Cwiczone umiejetnosci:** Lokalna inferencja LLM (Ollama), nawigacja po ekosystemie HuggingFace, API generowania obrazow, structured output z lokalnych modeli, rozumienie rozmiarow modeli i koncepcji kwantyzacji.

**Kluczowy wzorzec:** Lokalny LLM (Ollama) -> structured JSON -> generowanie obrazu na pozycje -> wizualne UI. Ta sama filozofia structured output co Projekt 1, inna infrastruktura.

---

## Konfiguracja i wymagania

### Przed kursem (studenci instaluja wczesniej)

1. **Python 3.11+** -- przez oficjalny installer albo pyenv
2. **VS Code** -- z rozszerzeniem Python + GitHub Copilot (darmowy tier wystarczy)
3. **Git** + **konto GitHub** -- do klonowania szablonow i pushowania projektow
4. **Klucz API Azure OpenAI lub Gemini** -- Azure OpenAI przez portal Azure (jesli masz subskrypcje), albo Gemini przez Google AI Studio (darmowy tier dostepny). Minimum jeden wymagany.
5. **Ollama** -- zainstaluj z ollama.com, sciagnij maly model: `ollama pull llama3.2:3b`

To wszystko. Bez Dockera. Bez LaTeX-a. Bez systemowych zależnosci poza Pythonem i Ollama.

### Zaleznosci per projekt (instalowane przez `pip install -r requirements.txt`)

| Projekt 1 (`genai-pdf-generator`) | Projekt 2 (`genai-menu-generator`) |
|-----------------------------------|------------------------------------|
| fastapi, uvicorn | fastapi, uvicorn |
| openai | ollama |
| reportlab | openai (do obrazow DALL-E) |
| qdrant-client | Pillow |
| numpy | |
| python-dotenv | python-dotenv |

### Zmienne srodowiskowe (`.env.example` w kazdym projekcie)

```
# Azure OpenAI (glowny)
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-5.3-chat              # Nazwa twojego deploymentu

# Gemini (alternatywa)
GEMINI_API_KEY=...

# Lokalne
OLLAMA_BASE_URL=http://localhost:11434       # Domyslne, zwykle nie trzeba zmieniac
```

---

## Notatki instruktora

### Zarzadzanie czasem

- Plany lekcji sa **celowo luzne** -- tematy i flow maja znaczenie, dokladny czas jest elastyczny.
- Lekcje 2 i 3 to po ~4 godziny. Prowadz je jako dwie sesje po 2h z przerwa, albo jedna dluga sesja -- co pasuje do twojego harmonogramu.
- **Jesli sie spozniasz: pominaj cwiczenia rozszerzajace i dodatek z embeddingami/wyszukiwaniem (Lekcja 2) albo polerowanie generowania obrazow (Lekcja 3). Nigdy nie pomijaj podstawowej funkcjonalnosci projektu.**
- **Nigdy nie spedzaj wiecej niz 10 minut na debugowaniu srodowiska jednego studenta.** Pomoz mu na przerwie albo po zajeciach.

### Strategia boilerplate'u

- Boilerplate (UI + routy) jest **swiety**. Studenci nie powinni go modyfikowac podczas zajec.
- Kazdy stub TODO powinien miec czytelny docstring tlumaczacy co funkcja ma robic, co dostaje i co powinna zwracac.
- Kod z rozwiazaniem (trzymaj go na prywatnym branchu albo prywatnym repo) to twoja "zlota referencja" na wypadek gdy studenci utkna.

### Typowe problemy i plany awaryjne

| Problem | Plan awaryjny |
|---------|---------------|
| Student nie ma klucza API | Miej 1-2 wspoldzielone klucze z limitami wydatkow jako backup |
| Ollama niezainstalowana / model nie sciagniety | Student uzywa API chmurowego do Projektu 2 (ten sam wzorzec) |
| Sciaganie Ollama zabija wifi | Powiedz studentom zeby instalowali + pullowali **przed zajeciami**. Pendrive jesli na zywo. |
| Laptop studenta nie udrzwignie lokalnych modeli | Fallback na API chmurowe do kazdego lokalnego zadania |
| LLM generuje zepsuty kod ReportLab | Moment edukacyjny, nie bug. Debugujcie razem. Pokaz logike retry. |
| Student zostaje w tyle z Projektem 1 | Embeddingi/wyszukiwanie to dodatek do wyciecia. Podstawowe generowanie PDF to priorytet. |

### Checklista przed lekcja

- [ ] Wszystkie dema przetestowane i dzialaja na twojej maszynie
- [ ] Klucze API doladowane i dzialaja
- [ ] Modele Ollama sciagniete (Lekcje 3-4)
- [ ] Szablony repo opublikowane i przetestowane -- swiezy klon -> `pip install` -> `uvicorn` musi dzialac
- [ ] Kod rozwiazania zweryfikowany wzgledem TODO w szablonach
- [ ] Plan awaryjny na kazda zewnetrzna zaleznosc (siec padla, API nie dziala itp.)

---

## Ocena i materialy do oddania

Bez egzaminow. Postep studenta mierzymy przez:

1. **Projekt 1:** Dzialajacy generator PDF z AI na ich GitHubie (bonus: z wyszukiwaniem semantycznym)
2. **Projekt 2:** Dzialajacy generator menu z AI na ich GitHubie
3. **Zaangazowanie:** Zadawanie pytan, eksperymentowanie, psucie rzeczy i ich naprawianie

Oba projekty sa **gotowe do portfolio**. Studenci moga je linkowac w CV/LinkedIn jako demonstracje praktycznych umiejetnosci inzynierskich GenAI.

---

*Ostatnia aktualizacja: Marzec 2026*
