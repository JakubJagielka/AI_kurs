# Lekcja 3: Swiat open-source -- HuggingFace, lokalne modele i Projekt 2

## Czesc 1 -- HuggingFace, lokalne modele i teoria (~2h)

### Ekosystem HuggingFace
- **Hub**: 500K+ modeli, datasetow, Spaces -- taki "GitHub dla AI"
- **Jak czytac Model Card**: architektura, liczba parametrow, licencja, benchmarki, ograniczenia
- **Biblioteka `transformers`**: `pipeline()` = najprostszy punkt wejscia dla malych modeli

### Ollama: lokalne LLM-y bez bolu
- Odpala skwantyzowane modele na CPU -- zero GPU
- Ten sam wzorzec API co OpenAI (to celowe)
- Kompromisy: wolniejszy, nizsza jakosc, ale za darmo i prywatny

### Modele audio
- **Whisper** (Speech-to-Text): model OpenAI, dziala lokalnie przez `transformers`
- **TTS**: Male modele moga generowac mowe z tekstu

### Pod maska: PyTorch i kwantyzacja

**Podstawy PyTorch:**
- Tensory = wielowymiarowe tablice (jak numpy ale z obsluga GPU)
- `model.generate()` = tokenizacja -> forward pass -> samplowanie -> detokenizacja

**Kluczowe liczby:**
| Model | Parametry | Rozmiar FP16 | Rozmiar INT4 |
|-------|-----------|--------------|--------------|
| 3B | 3 miliardy | ~6 GB | ~2 GB |
| 7B | 7 miliardow | ~14 GB | ~4 GB |
| 70B | 70 miliardow | ~140 GB | ~40 GB |

**Kwantyzacja**: Zmniejsz precyzje zeby zmniejszyc modele
- FP16 -> INT8 -> INT4 = mniejszy + szybszy, troche nizsza jakosc
- GGUF = format ktorego uzywa Ollama. Pre-skwantyzowane, zoptymalizowane pod CPU.

**Fine-tuning (teoria):**
- LoRA / QLoRA = trenuj maly adapter zamiast calego modelu
- Wymaga GPU + godzin trenowania
- **Nie potrzebujesz tego w 90% przypadkow** -- dobry prompting + RAG wystarcza

### Schemat decyzyjny
| Podejscie | Jakosc | Koszt | Prywatnosc | Szybkosc |
|-----------|--------|-------|------------|----------|
| Cloud API | super | $$$ | Niska | Szybko |
| Ollama lokalne | ok | Za darmo | Wysoka | Wolno |
| HF wyspecjalizowane | bardzo ok | Za darmo | Wysoka | Srednio |
| Hybryda | super | $$ | Srednia | Szybko |

---

## Czesc 2 -- Projekt 2: Generator menu (~2h)

### Architektura
```
Uzytkownik wybiera motyw -> Ollama (lokalny LLM) -> strukturyzowany JSON pozycji menu
                                                          ↓
                              DALL-E API -> obrazek jedzenia per pozycja
                                                          ↓
                              Wyswietl jako siatke wizualnych kart menu
```

### Kluczowe wzorce (te same co w Projekcie 1)
- Strukturyzowany output (tryb JSON) -- teraz z lokalnego modelu
- System prompt engineering do kreatywnego generowania
- Modele Pydantic dla bezpieczenstwa typow

---

## Kluczowe wnioski
1. HuggingFace Hub to twoje glowne miejsce do odkrywania modeli
2. Ollama sprawia ze lokalne LLM-y to pestka
3. Kwantyzacja pozwala duzym modelom zmiescic sie na malym sprzecie
4. Mieszaj chmure + lokalne zeby miec najlepsze z obu swiatow
