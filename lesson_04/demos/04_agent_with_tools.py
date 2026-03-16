"""Agent z wieloma narzedziami -- ten sam wzorzec, wiecej toolow, wiecej zabawy."""

import os
import json
import random
from datetime import datetime
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)


# --- Implementacje narzedzi ---

def get_current_time() -> str:
    return datetime.now().strftime("%A, %B %d, %Y at %H:%M:%S")


def calculate(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not all(c in allowed for c in expression):
        return "Blad: niedozwolone znaki"
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Blad: {e}"


def read_file(filepath: str) -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if len(content) > 2000:
            return content[:2000] + "\n... (uciete)"
        return content
    except FileNotFoundError:
        return f"Plik nie znaleziony: {filepath}"
    except Exception as e:
        return f"Blad czytania pliku: {e}"


def roll_dice(sides: int = 6, count: int = 1) -> str:
    rolls = [random.randint(1, sides) for _ in range(count)]
    return f"Rzucono {count}d{sides}: {rolls} (suma: {sum(rolls)})"


def word_count(text: str) -> str:
    words = len(text.split())
    chars = len(text)
    return f"Slowa: {words}, Znaki: {chars}"


# --- Rejestr narzedzi ---

TOOL_MAP = {
    "get_current_time": get_current_time,
    "calculate": calculate,
    "read_file": read_file,
    "roll_dice": roll_dice,
    "word_count": word_count,
}

TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current date and time",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a math expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "e.g. '2 + 2' or '100 / 7'"},
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the contents of a text file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {"type": "string", "description": "Path to the file to read"},
                },
                "required": ["filepath"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "roll_dice",
            "description": "Roll dice for games or random decisions",
            "parameters": {
                "type": "object",
                "properties": {
                    "sides": {"type": "integer", "description": "Number of sides (default 6)"},
                    "count": {"type": "integer", "description": "Number of dice (default 1)"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "word_count",
            "description": "Count words and characters in a text",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Text to count"},
                },
                "required": ["text"],
            },
        },
    },
]


# --- Petla agenta ---

def agent(user_input: str, max_steps: int = 10):
    print(f"\nUser: {user_input}\n")

    messages = [
        {"role": "system", "content": "You are a helpful assistant with tools. Use them when needed."},
        {"role": "user", "content": user_input},
    ]

    for step in range(max_steps):
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
            messages=messages,
            tools=TOOLS_SCHEMA,
        )

        msg = response.choices[0].message

        if not msg.tool_calls:
            print(f"Agent: {msg.content}")
            return

        messages.append(msg)

        for tc in msg.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments) if tc.function.arguments else {}
            print(f"  [tool] {name}({args})")

            fn = TOOL_MAP.get(name)
            result = fn(**args) if fn else f"Nieznane narzedzie: {name}"
            print(f"     -> {result}")

            messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})

    print("Agent: Osiagnieto max krokow.")


# --- Przetestuj ---
agent("What time is it, and roll me 3d20 for my D&D character")
agent("Read the file '../README.md' and tell me how many words it has")
agent("Calculate 2^10 and also tell me what day of the week it is")
