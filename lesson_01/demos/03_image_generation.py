"""Generowanie obrazu z prompta tekstowego przez Google Imagen 4.0."""

# pip install google-genai

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


def generate():
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    prompt = "A cozy coffee shop on a rainy day, watercolor style"
    print(f"Prompt: {prompt}")
    print("Generowanie obrazu przez Imagen 4.0...")

    result = client.models.generate_images(
        model="models/imagen-4.0-generate-001",
        prompt=prompt,
        config=dict(
            number_of_images=1,
            output_mime_type="image/jpeg",
            person_generation="ALLOW_ADULT",
            aspect_ratio="1:1",
            image_size="1K",
        ),
    )

    if not result.generated_images:
        print("Nie wygenerowano zadnych obrazow.")
        return

    if len(result.generated_images) != 1:
        print("Liczba wygenerowanych obrazow nie zgadza sie z zamowiona.")

    output_dir = os.path.dirname(__file__)
    for n, generated_image in enumerate(result.generated_images):
        filepath = os.path.join(output_dir, f"generated_image_{n}.jpg")
        generated_image.image.save(filepath)
        print(f"Zapisano: {filepath}")

    print("Gotowe! Sprawdz wygenerowany plik.")


if __name__ == "__main__":
    generate()

# --- Sprobuj sam ---
# Zmien prompt. Przetestuj rozne style: "pixel art", "oil painting", "photograph".
# Zmien aspect_ratio na "16:9" lub "9:16". Zmien number_of_images na 2-4.
