import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not found in .env file")

client = ElevenLabs(api_key=API_KEY)


def generate_speech(text, voice_id, output_path):

    print("\nGenerating speech...")

    audio = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id="eleven_v3",
        output_format="mp3_44100_128"
    )

    with open(output_path, "wb") as output_file:

        for chunk in audio:
            output_file.write(chunk)

    print("\n========== AUDIO GENERATED ==========")
    print("Output:", output_path)
    print("=====================================\n")


if __name__ == "__main__":

    text = "Hello, my name is Ankita. Welcome to my multimedia project."

    # Replace this with your actual Voice B ID
    voice_id = "YOUR_VOICE_B_ID"

    output_path = "output/voice_b_output.mp3"

    try:

        generate_speech(
            text,
            voice_id,
            output_path
        )

    except Exception as e:
        print("ERROR:", e)