"""HuggingFace pipeline() -- analiza sentymentu w kilku linijkach."""

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

texts = [
    "I love this course, it's amazing!",
    "The weather is terrible today.",
    "Python is a programming language.",
    "This is the best pizza I've ever had!",
    "I'm not sure how I feel about this.",
]

print("Wyniki analizy sentymentu:")
print("-" * 50)

results = classifier(texts)
for text, result in zip(texts, results):
    label = "+" if result["label"] == "POSITIVE" else "-"
    print(f"[{label}] [{result['label']:>8}] ({result['score']:.2%}) -- {text}")

# --- Sprobuj sam ---
# Przetestuj inne pipeline'y:
#   pipeline("ner")              -- rozpoznawanie encji (Named Entity Recognition)
#   pipeline("summarization")    -- streszczanie tekstu
#   pipeline("translation_en_to_fr") -- tlumaczenie
