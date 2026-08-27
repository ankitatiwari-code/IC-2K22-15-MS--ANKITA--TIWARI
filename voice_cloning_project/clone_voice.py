
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not found in .env file")

client = ElevenLabs(api_key=API_KEY)


def clone_voice(audio_path, voice_name):

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print(f"\nCreating voice clone: {voice_name}")

    with open(audio_path, "rb") as audio_file:

        voice = client.voices.ivc.create(
            name=voice_name,
            files=[audio_file]
        )

    voice_id = voice.voice_id

    print("\n========== VOICE CREATED ==========")
    print("Voice Name:", voice_name)
    print("Voice ID:", voice_id)
    print("===================================\n")

    return voice_id


if __name__ == "__main__":

    audio_path = "input/voice_b.mp3"

    try:

        voice_id = clone_voice(
            audio_path,
            "My Voice B"
        )

        print("Save this Voice ID:")
        print(voice_id)

    except Exception as e:
        print("ERROR:", e)