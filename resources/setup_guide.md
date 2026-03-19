# Poradnik przygotowania do kursu

Zainstaluj wszystko **przed** pierwszymi zajeciami. To zajmie ~15 minut.

---

## 1. Python 3.11+

**Sprawdz czy masz:**
```bash
python --version
```

**Zainstaluj jesli potrzeba:**
- Windows: https://www.python.org/downloads/ (zaznacz "Add to PATH")
- Mac: `brew install python@3.12`
- Linux: `sudo apt install python3.12`

---

## 2. VS Code

Pobierz: https://code.visualstudio.com/

**Wymagane rozszerzenia:**
- Python (Microsoft)
- GitHub Copilot (darmowy tier wystarczy)

---

## 3. Git + GitHub

**Git:** https://git-scm.com/downloads

**Konto GitHub:** https://github.com (jesli nie masz)

**Weryfikacja:**
```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

## 4. Klucze API (przynajmniej jeden wymagany)

### Opcja A: Azure OpenAI (glowna)
1. Wejdz na https://portal.azure.com
2. Stworz zasob Azure OpenAI
3. Wdraz model `gpt-5.3-chat`
4. Pobierz klucz API i endpoint

### Opcja B: Google Gemini (alternatywna, darmowy tier)
1. Wejdz na https://aistudio.google.com/
2. Pobierz klucz API
3. Darmowy tier: w zupelnosci wystarczy na ten kurs

> **Uwaga:** Klucz Gemini jest tez potrzebny do demo generowania obrazow (Imagen 4.0)
> oraz do porownania providerow (demo 09). Polecam miec oba klucze.

---

## 5. Plik `.env` -- konfiguracja kluczy API

W katalogu glownym repozytorium (`AI_kurs/`) stworz plik `.env`:

```ini
# Azure OpenAI
AZURE_OPENAI_API_KEY=twoj-klucz-azure
AZURE_OPENAI_ENDPOINT=https://twoj-zasob.cognitiveservices.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-5.3-chat
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small

# Google Gemini (do generowania obrazow + porownanie providerow)
GEMINI_API_KEY=twoj-klucz-gemini
```

**Wazne:**
- Plik `.env` **nigdy** nie powinien trafic na Githuba -- dodaj go do `.gitignore`
- Kazdy demo skrypt automatycznie czyta ten plik dzieki `python-dotenv`

---

## 6. Ollama (potrzebne do lekcji 3-4)

**Instalacja:** https://ollama.com/download

**Pobierz maly model:**
```bash
ollama pull llama3.2:3b
```

**Weryfikacja:**
```bash
ollama run llama3.2:3b "Hello, how are you?"
```

Download modelu to ~2 GB. **Zrob to w domu**, nie na wifi w sali.

---

## 7. Setup srodowiska (krok po kroku)

```bash
# 1. Sklonuj repozytorium
git clone https://github.com/JakubJagielka/AI_kurs.git
cd AI_kurs

# 2. Stworz wirtualne srodowisko
python -m venv venv

# 3. Aktywuj je
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Windows (cmd):
venv\Scripts\activate.bat
# Mac/Linux:
source venv/bin/activate

# 4. Zainstaluj WSZYSTKIE zaleznosci jednym poleceniem
pip install -r requirements.txt

# 5. Skopiuj i uzupelnij plik .env (patrz sekcja 5 powyzej)
# Jesli nie masz pliku .env -- stworz go i wklej swoje klucze API

# 6. Sprawdz czy dziala -- odpal pierwsze demo
python lesson_01/demos/01_first_llm_call.py
```

### Co jest w `requirements.txt`?

| Pakiet | Do czego | Lekcje |
|--------|----------|--------|
| `openai` | Azure OpenAI SDK | 1-4 |
| `python-dotenv` | Ladowanie `.env` | 1-4 |
| `numpy` | Wektory, cosine similarity | 1-2 |
| `google-genai` | Imagen 4.0 (generowanie obrazow) | 1 |
| `google-generativeai` | Gemini chat API | 1 |
| `transformers` + `torch` | Modele HuggingFace lokalnie | 3 |
| `datasets` + `scipy` | Dane + zapis audio | 3 |
| `ollama` | Klient Python dla Ollama | 3-4 |
| `mcp` | Model Context Protocol SDK | 4 |

> **Tip:** Jesli chcesz zainstalowac tylko pakiety do lekcji 1-2 (szybciej, bez torch):
> ```bash
> pip install openai python-dotenv numpy google-genai google-generativeai
> ```

---

## Rozwiazywanie problemow

| Problem | Rozwiazanie |
|---------|-------------|
| `python` nie znaleziony | Sprobuj `python3`. Albo przeinstaluj z zaznaczonym "Add to PATH". |
| `pip install` nie dziala | Sprobuj `pip install --upgrade pip` najpierw |
| Ollama nie startuje | Sprawdz czy dziala: `ollama list`. Zrestartuj apke. |
| Klucz API nie dziala | Sprawdz biale znaki na koncu. Zweryfikuj w Azure Portal / AI Studio. |
| Git push odrzucony | Upewnij sie ze sklonowales SWOJA kopie, nie template bezposrednio |

---

## Checklist

- [ ] Python 3.11+ zainstalowany i dziala
- [ ] VS Code zainstalowany z rozszerzeniami Python + Copilot
- [ ] Git zainstalowany, konto GitHub stworzone
- [ ] Plik `.env` stworzony z kluczami API (Azure OpenAI + Gemini)
- [ ] `pip install -r requirements.txt` przeszlo bez bledow
- [ ] Ollama zainstalowane, model `llama3.2:3b` pobrany
- [ ] `python lesson_01/demos/01_first_llm_call.py` dziala
- [ ] Gotowy zeby budowac fajne rzeczy z AI
