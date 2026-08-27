import os

from transcribe import transcribe_audio
from clone_voice import clone_voice
from text_to_speech import generate_speech


SOURCE_AUDIO = r"input\Amitabh_voice.m4a"
VOICE_B_AUDIO = r"input\Shahrukh-voice.m4a"

OUTPUT_AUDIO = "output/final_voice_b.mp3"


def main():

    print("\n")
    print("==============================================")
    print("       AI VOICE CLONING SYSTEM")
    print("==============================================")

    # ------------------------------------------
    # STEP 1: TRANSCRIBE SOURCE AUDIO
    # ------------------------------------------

    print("\n[1] Transcribing source audio...")

    text = transcribe_audio(SOURCE_AUDIO)

    # ------------------------------------------
    # STEP 2: CREATE / USE TARGET VOICE
    # ------------------------------------------

    print("\n[2] Creating target voice...")

    voice_id = clone_voice(
        VOICE_B_AUDIO,
        "Target Voice B"
    )

    # ------------------------------------------
    # STEP 3: GENERATE SPEECH
    # ------------------------------------------

    print("\n[3] Generating speech in target voice...")

    generate_speech(
        text,
        voice_id,
        OUTPUT_AUDIO
    )

    # ------------------------------------------
    # COMPLETE
    # ------------------------------------------

    print("\n==============================================")
    print("              PROCESS COMPLETE")
    print("==============================================")

    print("\nOriginal Audio:")
    print(SOURCE_AUDIO)

    print("\nTranscribed Text:")
    print(text)

    print("\nGenerated Audio:")
    print(OUTPUT_AUDIO)

    print("\n==============================================\n")


if __name__ == "__main__":
    main()