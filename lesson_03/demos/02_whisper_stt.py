"""Speech-to-Text z Whisper -- transkrypcja audio lokalnie."""

from transformers import pipeline

transcriber = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
)

audio_file = "sample_audio/test_clip.wav"

print(f"Transkrybuje: {audio_file}")
print("-" * 40)

result = transcriber(audio_file)
print(f"Tekst: {result['text']}")

# --- Sprobuj sam ---
# Nagraj wlasny plik .wav i go transkrybuj!
# Mozesz uzyc: python -c "import sounddevice; ..."  albo dowolnej apki do nagrywania.
#
# Przetestuj rozne rozmiary Whispera:
#   openai/whisper-tiny   -- najszybszy, najnizsza jakosc
#   openai/whisper-small  -- dobry balans
#   openai/whisper-medium -- lepsza jakosc, wolniejszy
#   openai/whisper-large  -- najlepsza jakosc, potrzebuje wiecej RAM
