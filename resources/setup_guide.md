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

---

## 5. Ollama (potrzebne do lekcji 3-4)

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

## 6. Setup srodowiska (per projekt)

Kiedy zaczynamy kazdy projekt, odpalasz:

```bash
# Sklonuj template repo
git clone https://github.com/YOUR-USERNAME/genai-pdf-generator
cd genai-pdf-generator

# Stworz wirtualne srodowisko
python -m venv venv

# Aktywuj je
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Zainstaluj zaleznosci
pip install -r requirements.txt

# Skopiuj zmienne srodowiskowe
cp .env.example .env
# Potem edytuj .env swoimi kluczami API
```

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
- [ ] Przynajmniej jeden klucz API dziala (Azure OpenAI lub Gemini)
- [ ] Ollama zainstalowane, model `llama3.2:3b` pobrany
- [ ] Gotowy zeby budowac fajne rzeczy z AI
