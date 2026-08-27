import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not found in .env file")

client = ElevenLabs(api_key=API_KEY)


def transcribe_audio(audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print("\nTranscribing audio...")

    with open(audio_path, "rb") as audio_file:
        transcription = client.speech_to_text.convert(
            file=audio_file,
            model_id="scribe_v2"
        )

    text = transcription.text

    print("\n========== TRANSCRIPTION ==========")
    print(text)
    print("===================================\n")

    return text


if __name__ == "__main__":

    audio_path = "input\Amitabh_voice.m4a"

    try:
        transcribe_audio(audio_path)

    except Exception as e:
        print("ERROR:", e)