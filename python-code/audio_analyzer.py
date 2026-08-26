import os
from mutagen import File


def analyze_audio(file_path):

    if not os.path.exists(file_path):
        print("Error: File not found.")
        return

    try:
        audio = File(file_path)

        if audio is None:
            print("Error: Unable to read this audio file.")
            return

        info = audio.info

        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        duration = getattr(info, "length", 0)
        bitrate = getattr(info, "bitrate", 0)
        channels = getattr(info, "channels", 0)
        sample_rate = getattr(info, "sample_rate", 0)

        print("=" * 40)
        print("       AUDIO METADATA REPORT")
        print("=" * 40)

        print(f"\nFile Name       : {file_name}")
        print(f"File Size       : {file_size} bytes")
        print(f"Format          : {type(audio).__name__}")
        print(f"Duration        : {duration:.2f} seconds")

        print("\nAUDIO")
        print("-" * 32)

        print(f"Codec           : {type(info).__name__}")
        print(f"Channels        : {channels}")
        print(f"Sampling Rate   : {sample_rate} Hz")
        print(f"Bit Rate        : {bitrate} bps")

        print("\nMETADATA")
        print("-" * 32)

        if audio.tags:
            for key, value in audio.tags.items():
                print(f"{key:<20}: {value}")
        else:
            print("No additional metadata available.")

    except Exception as e:
        print("Error:", e)


# Main program
file_path = input("\nEnter audio file path: ").strip()

analyze_audio(file_path)