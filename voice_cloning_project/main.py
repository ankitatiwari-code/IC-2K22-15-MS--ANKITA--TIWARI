
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from clone_voice import clone_voice

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    raise ValueError(
        "ELEVENLABS_API_KEY not found. Check your .env file."
    )

client = ElevenLabs(api_key=api_key)

voice_id = clone_voice(
    "input/Amitabh_voice.m4a",
    "Target Voice B",
    client
)

print("Voice ID:", voice_id)
