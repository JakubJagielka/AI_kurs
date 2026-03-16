"""Prosty ReAct agent loop -- bez frameworka, tylko petla while.

Tak dzialaja agenci pod spodem. Kazdy framework (LangChain, CrewAI, itd.)
to po prostu fancy wrapper wokol tego samego wzorca.
"""

import os
import json
from datetime import datetime
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# --- Definiujemy narzedzia ---

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
                    "expression": {"type": "string", "description": "Math expression"},
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_knowledge",
            "description": "Search a knowledge base for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                },
                "required": ["query"],
            },
        },
    },
]


def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not all(c in allowed for c in expression):
        return "Blad: niedozwolone znaki"
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Blad: {e}"


def search_knowledge(query: str) -> str:
    """Fake baza wiedzy -- w realnym zyciu to bylby vector DB albo API."""
    knowledge = {
        "python": "Python is a high-level programming language created by Guido van Rossum in 1991.",
        "fastapi": "FastAPI is a modern Python web framework for building APIs, created by Sebastian Ramirez.",
        "ollama": "Ollama is a tool for running large language models locally on your machine.",
    }
    query_lower = query.lower()
    for key, value in knowledge.items():
        if key in query_lower:
            return value
    return f"Brak wynikow dla: {query}"


TOOL_FUNCTIONS = {
    "get_current_time": get_current_time,
    "calculate": calculate,
    "search_knowledge": search_knowledge,
}


# --- Petla agenta ---

def run_agent(user_input: str, max_iterations: int = 5):
    print(f"\n{'='*60}")
    print(f"User: {user_input}")
    print(f"{'='*60}")

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant with access to tools. Use them when needed. Think step by step.",
        },
        {"role": "user", "content": user_input},
    ]

    for i in range(max_iterations):
        print(f"\n--- Krok agenta {i+1} ---")

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
            messages=messages,
            tools=TOOLS_SCHEMA,
        )

        message = response.choices[0].message

        # Brak tool calls = agent skonczyl, zwracamy finalna odpowiedz
        if not message.tool_calls:
            print(f"Agent: {message.content}")
            return message.content

        # Przetwarzamy kazde wywolanie narzedzia
        messages.append(message)

        for tool_call in message.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments) if tool_call.function.arguments else {}

            print(f"  Wola: {fn_name}({fn_args})")

            fn = TOOL_FUNCTIONS.get(fn_name)
            if fn:
                result = fn(**fn_args)
            else:
                result = f"Nieznane narzedzie: {fn_name}"

            print(f"  Wynik: {result}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result),
            })

    print("Agent: Osiagnieto maksymalna liczbe iteracji.")
    return "Nie udalem sie ukonczyc zadania w czasie."


# Testujemy agenta
run_agent("What time is it and what's 42 * 58?")
run_agent("Tell me about FastAPI")
run_agent("What's the time, and also calculate how many seconds are in 3.5 hours")
