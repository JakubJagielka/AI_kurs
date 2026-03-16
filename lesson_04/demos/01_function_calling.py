"""Function calling -- LLM decyduje sie uzyc kalkulatora zamiast zgadywac."""

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

# Definiujemy narzedzie kalkulatora
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform a math calculation. Use this for any arithmetic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression to evaluate, e.g. '1547 * 382'",
                    },
                },
                "required": ["expression"],
            },
        },
    }
]


def calculate(expression: str) -> str:
    """Bezpiecznie ewaluuj wyrazenie matematyczne."""
    allowed = set("0123456789+-*/(). ")
    if not all(c in allowed for c in expression):
        return "Blad: niedozwolone znaki w wyrazeniu"
    try:
        result = eval(expression)  # bezpieczne -- zwalidowalismy znaki
        return str(result)
    except Exception as e:
        return f"Blad: {e}"


def run_with_tools(user_message: str):
    print(f"User: {user_message}")

    messages = [{"role": "user", "content": user_message}]

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
        messages=messages,
        tools=tools,
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        print(f"  -> LLM wola: {tool_call.function.name}({args})")

        result = calculate(**args)
        print(f"  -> Wynik: {result}")

        # Wysylamy wynik z powrotem po odpowiedz w naturalnym jezyku
        messages.append(message)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        })

        final = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
            messages=messages,
            tools=tools,
        )
        print(f"  -> Odpowiedz: {final.choices[0].message.content}")
    else:
        print(f"  -> Odpowiedz: {message.content}")

    print()


# Testujemy!
run_with_tools("What is 1547 * 382?")
run_with_tools("What's the capital of France?")  # nie powinno uzyc narzedzia
run_with_tools("If I have 3 boxes with 147 items each, how many total?")
