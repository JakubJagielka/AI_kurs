"""Web search grounding -- LLM-y nie znaja dzisiejszych wiadomosci, ale mozesz dac im narzedzia ktore znaja."""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Najpierw: pytamy bez groundingu -- LLM odmowi albo zhallucynuje
print("=== Bez web search ===")
response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
    messages=[
        {"role": "user", "content": "What are today's top tech news headlines?"},
    ],
)
print(response.choices[0].message.content)
print()

# Teraz: z web search groundingiem (Azure OpenAI z Bing grounding)
# Uwaga: wymaga zasobu Bing Search podlaczonego do Azure OpenAI
print("=== Z web search groundingiem ===")
try:
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.3-chat"),
        messages=[
            {"role": "user", "content": "What are today's top tech news headlines?"},
        ],
        extra_body={
            "data_sources": [
                {
                    "type": "bing_grounding",
                    "parameters": {
                        "connection_id": os.getenv("BING_CONNECTION_ID", ""),
                    },
                }
            ]
        },
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Web search nie skonfigurowany: {e}")
    print("Spokoj -- chodzi o to ze LLM-y potrzebuja zewnetrznych narzedzi do danych real-time.")
    print("Podlaczylbys Bing Search albo uzywal serwisu jak Perplexity.")
