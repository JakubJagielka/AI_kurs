# Sciaga modelowa -- szybki przeglad

## Generowanie tekstu (LLM-y)

| Model | Rozmiar | Gdzie odpalac | Najlepszy do |
|-------|---------|--------------|--------------|
| gpt-5.3-chat | ~200B? | Azure OpenAI API | Najlepsza jakosc, zlozony reasoning |
| gpt-5.3-chat-mini | ~? | Azure OpenAI API | Szybki + tani, dobra jakosc |
| Gemini 2.0 Flash | ~? | Google AI API | Szybki, dobry darmowy tier |
| Llama 3.2 3B | 3B | Ollama (CPU ok) | Lokalny, maly, przyzwoita jakosc |
| Qwen 2.5 3B | 3B | Ollama (CPU ok) | Lokalny, swietny wielojezycznie |
| Mistral 7B | 7B | Ollama (potrzebne 8GB+ RAM) | Lokalny, dobra jakosc |

## Embeddingi

| Model | Wymiary | Gdzie odpalac | Uwagi |
|-------|---------|--------------|-------|
| text-embedding-3-small | 1536 | Azure OpenAI API | Tani, szybki, swietna jakosc |
| text-embedding-3-large | 3072 | Azure OpenAI API | Wyzsza jakosc, kosztuje wiecej |
| all-MiniLM-L6-v2 | 384 | Lokalnie (HuggingFace) | Za darmo, dziala na CPU |

## Generowanie obrazkow

| Model | Gdzie odpalac | Jakosc | Szybkosc |
|-------|--------------|--------|----------|
| DALL-E 3 | Azure OpenAI API | Swietna | ~10s |
| Stable Diffusion XL | Lokalnie (potrzebny GPU) | Dobra | ~30s (GPU) / minuty (CPU) |
| Flux.1 Schnell | Lokalnie (potrzebny GPU) | Dobra | ~5s (GPU) |

## Speech-to-Text

| Model | Rozmiar | Gdzie odpalac | Uwagi |
|-------|---------|--------------|-------|
| Whisper tiny | 39M | Lokalnie (CPU) | Szybki ale mniej dokladny |
| Whisper small | 244M | Lokalnie (CPU) | Dobry balans |
| Whisper medium | 769M | Lokalnie (CPU) | Lepsza dokladnosc |
| Whisper large-v3 | 1.5B | Lokalnie (zalecany GPU) | Najlepsza dokladnosc |

## Text-to-Speech

| Model | Gdzie odpalac | Uwagi |
|-------|--------------|-------|
| SpeechT5 | Lokalnie (CPU) | Dobra jakosc, potrzebuje speaker embeddingow |
| Azure TTS | Azure API | Najlepsza jakosc, duzo glosow |

## Klasyfikacja / NLP

| Zadanie | Model | Gdzie odpalac |
|---------|-------|--------------|
| Sentyment | distilbert-base-uncased-finetuned-sst-2 | Lokalnie (CPU) |
| NER | dslim/bert-base-NER | Lokalnie (CPU) |
| Streszczanie | facebook/bart-large-cnn | Lokalnie (CPU, wolno) |
| Tlumaczenie | Helsinki-NLP/opus-mt-en-{lang} | Lokalnie (CPU) |

---

**Zasada ogolna**: Cloud API po najlepsza jakosc + szybkosc. Lokalne modele kiedy zalezy ci na prywatnosci albo chcesz oszczedzic. Wyspecjalizowane modele HuggingFace do konkretnych zadan (NER, sentyment, STT).
