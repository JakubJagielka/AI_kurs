# Lekcja 1: Krajobraz GenAI i opanowanie API

## Krajobraz (~15min)

### Czym sa LLM-y?
- Large Language Models = sieci neuronowe wytrenowane na ogromnych ilosciach tekstu
- Przewiduja nastepny token (kawalek slowa) na podstawie kontekstu
- To nie jest "myslenie" — to dopasowywanie wzorcow na kosmiczna skale

### Kluczowe pojecia
- **Tokeny**: Tekst podzielony na kawalki (~4 znaki na token w angielskim)
- **Okno kontekstowe**: Ile tekstu model "widzi" naraz (128K tokenow dla gpt-5.3-chat)
- **Temperature**: 0 = determinizm, 1 = kreatywnosc, 2 = chaos
- **System prompt**: Instrukcje ktore ksztaltuja zachowanie modelu

### Jak dzialaja Transformery (60 sekund)
```
Tekst wejsciowy -> Tokenizacja -> Embeddingi -> Warstwy Attention -> Prawdopodobienstwa -> Samplowanie -> Detokenizacja -> Tekst wyjsciowy
```
To tyle. Attention = "na ktore slowa powinienem sie skupic zeby przewidziec nastepne?"

### Dostawcy chmurowi
| Dostawca | Modele | Cennik |
|----------|--------|--------|
| Azure OpenAI | gpt-5.3-chat, DALL-E 3, text-embedding-3-small | Plac za tokeny |
| Google Gemini | Gemini 2.0 Flash, Gemini 2.0 Pro | Darmowy tier |
| Open-source (Ollama) | Llama 3.2, Qwen 2.5, Mistral | Za darmo, dziala lokalnie |

---

## Glowne dema (~20min)

Przejdzcie przez dema 01-04 ze studentami. Niech zmieniaja prompty i patrza co sie dzieje.

Kluczowe momenty:
- Zmiana temperature z 0 na 1.5 — output idzie od nudnego przez kreatywny do odjechany
- Vision API — moment "komputery teraz widza"
- Embeddingi — "tak wlasnie wyszukiwarki rozumieja znaczenie"

---

## Poza Hello World (~20min)

Dema 05-07 pokazuja prawdziwe inzynierskie wzorce:
- **Config patterns**: Nigdy nie hardkoduj kluczy API. Nigdy.
- **Function calling**: LLM sam decyduje KIEDY uzyc narzedzia. To fundament agentow.
- **Web search grounding**: LLM-y nie wiedza jaki jest dzisiaj dzien. Daj im narzedzia ktore wiedza.
- **Structured JSON output** (demo 10): LLM zwraca JSON z gwarantowanym schematem. Dwa podejscia:
  - `response_format=json_object` -- LLM zwraca JSON, ale nie gwarantujesz jakie klucze dostaniesz
  - `json_schema` (strict mode) -- definiujesz dokladny schemat, LLM MUSI sie dostosowac
  - Praktycznie: ekstrakcja danych z nieustrukturyzowanego tekstu -> czysty JSON -> odczytujesz klucze
  - "Tak laczycie LLM-y z reszta kodu. Nie parsujecie stringow -- uzywacie `json.loads()` i gotowe."

---

## Zaawansowane (jesli starczy czasu)
- Czat z pamięcią konwersacji (demo 08): LLM NIE ma wbudowanej pamieci. To programista trzyma liste messages i wysyla ja CALA za kazdym razem. Studenci podaja imie, potem pytaja "jak mam na imie?" i widza ze dziala. Na koniec: pokaz rosnaca liste -- to dlatego dlugie konwersacje kosztuja wiecej tokenow.
- Porownanie providerow: Nie ma jednego najlepszego modelu. Dobieraj pod zadanie.

---

## Praca domowa
1. Odpal wszystkie glowne dema (01-07, 10)
2. Sprobuj zaawansowanych (08-09) jesli cie ciagnie
3. Zainstaluj Ollame: https://ollama.com — sciagnij `llama3.2:3b`
4. Upewnij sie ze twoj klucz API dziala!
