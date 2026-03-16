# Minimalny serwer MCP -- czytnik plikow

Prosty serwer MCP ktory wystawia dwa narzedzia:
- **read_file** -- czytaj zawartosc dowolnego pliku tekstowego
- **list_directory** -- listuj pliki/foldery w katalogu

## Setup

```bash
pip install mcp
```

## Odpal standalone (do testow)

```bash
python server.py
```

Serwer komunikuje sie przez stdin/stdout uzywajac JSON-RPC (protokol MCP).

## Podlacz do Claude Desktop

Dodaj to do configa Claude Desktop (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "file-reader": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

Zrestartuj Claude Desktop. Zobaczysz dostepne narzedzia w UI.

## Podlacz do VS Code

Dodaj do ustawien VS Code:

```json
{
  "mcp": {
    "servers": {
      "file-reader": {
        "command": "python",
        "args": ["path/to/server.py"]
      }
    }
  }
}
```

## Jak to dziala

1. Host MCP (Claude Desktop / VS Code) uruchamia ten serwer jako subprocess
2. Pyta "jakie masz narzedzia?" -- zwracamy `read_file` i `list_directory`
3. Kiedy AI decyduje sie uzyc narzedzia, host wysyla request `call_tool`
4. Wykonujemy go i zwracamy wynik
5. AI uzywa wyniku zeby sformulowac odpowiedz

I tyle. MCP to po prostu standard na function calling miedzy roznymi hostami AI.
