"""Function calling -- daj LLM-owi narzedzie i patrz jak decyduje sie go uzyc."""

import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Definiujemy narzedzie ktore LLM moze uzyc
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                },
                "required": ["city"],
            },
        },
    }
]


# Nasza fake funkcja pogodowa (w realnym zyciu wola API pogodowe)
def get_weather(city: str) -> str:
    fake_weather = {
        "London": "Deszczowo, 12C",
        "Tokyo": "Slonecznie, 22C",
        "New York": "Pochmurno, 18C",
    }
    return fake_weather.get(city, f"Brak danych dla {city}")


# Krok 1: Pytamy LLM o cos co wymaga danych pogodowych
response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
    messages=[
        {"role": "user", "content": "What's the weather like in Tokyo?"},
    ],
    tools=tools,
)

message = response.choices[0].message

# Krok 2: Sprawdzamy czy LLM chce wywolac narzedzie
if message.tool_calls:
    tool_call = message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    print(f"LLM chce wywolac: {tool_call.function.name}({args})")

    # Krok 3: Wykonujemy narzedzie
    result = get_weather(**args)
    print(f"Wynik narzedzia: {result}")

    # Krok 4: Wysylamy wynik z powrotem do LLM
    follow_up = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
        messages=[
            {"role": "user", "content": "What's the weather like in Tokyo?"},
            message.model_dump(),
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            },
        ],
        tools=tools,
    )
    print(f"\nOstateczna odpowiedz: {follow_up.choices[0].message.content}")
else:
    print(f"LLM answered directly: {message.content}")
