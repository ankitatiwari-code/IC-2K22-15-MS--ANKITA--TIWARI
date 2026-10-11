
import io
from elevenlabs.client import ElevenLabs


def clone_voice(audio_file, voice_name, client):
    """
    Create an Instant Voice Clone using ElevenLabs.

    audio_file: Path to an audio file or binary audio stream.
    voice_name: Name for the new voice.
    client: An authenticated ElevenLabs client.
    """

    print(f"Creating voice clone: {voice_name}")

    with open(audio_file, "rb") as audio:
        voice = client.voices.ivc.create(
            name=voice_name,
            files=[audio]
        )

    print("Voice clone created successfully.")
    return voice.voice_id
