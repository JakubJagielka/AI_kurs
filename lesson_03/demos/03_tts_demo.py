"""Demo Text-to-Speech -- generowanie mowy z tekstu."""

from transformers import pipeline
import scipy.io.wavfile
import numpy as np

synthesizer = pipeline("text-to-speech", model="microsoft/speecht5_tts")

# SpeechT5 potrzebuje speaker embeddingow -- uzywamy domyslnego
from datasets import load_dataset

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = embeddings_dataset[7306]["xvector"]
speaker_embedding = np.array(speaker_embedding).reshape(1, -1)

text = "Hello! Welcome to the practical GenAI engineering course."
print(f"Generuje mowe dla: '{text}'")

result = synthesizer(text, forward_params={"speaker_embeddings": speaker_embedding})

output_file = "output_speech.wav"
scipy.io.wavfile.write(output_file, rate=result["sampling_rate"], data=result["audio"])

print(f"Zapisano do: {output_file}")
print("Odtworz dowolnym odtwarzaczem!")

# --- Sprobuj sam ---
# Zmien tekst. Sprobuj dluzszych zdan.
# Sprobuj roznych speaker embeddingow (zmien indeks: embeddings_dataset[0], [100], itd.)
