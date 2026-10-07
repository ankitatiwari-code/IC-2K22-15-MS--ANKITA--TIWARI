import os
from mutagen import File


def format_file_size(size):
    """Convert bytes into a readable file size."""

    if size < 1024:
        return f"{size} Bytes"

    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"

    else:
        return f"{size / (1024 * 1024):.2f} MB"


def analyze_audio(file_path):
    """
    Analyze an audio file and return metadata as a dictionary.
    """

    # Check if file exists
    if not os.path.isfile(file_path):
        return {
            "error": "File not found"
        }

    try:

        # Read audio file using Mutagen
        audio = File(file_path)

        if audio is None:
            return {
                "error": "Unable to read this audio file"
            }

        info = audio.info

        # Basic file information
        file_name = os.path.basename(file_path)

        file_size = os.path.getsize(file_path)

        extension = os.path.splitext(file_path)[1].lower()

        # Audio information
        duration = getattr(info, "length", 0)

        bitrate = getattr(info, "bitrate", 0)

        channels = getattr(info, "channels", 0)

        sample_rate = getattr(info, "sample_rate", 0)

        # Codec / format
        audio_format = type(audio).__name__

        codec = type(info).__name__

        # Metadata
        metadata = {}

        if audio.tags:

            for key, value in audio.tags.items():

                value_string = str(value)

                # Prevent extremely long metadata
                if len(value_string) > 200:
                    value_string = value_string[:200] + "..."

                metadata[str(key)] = value_string

        else:

            metadata["Information"] = "No additional metadata available."

        # Create result
        result = {

            "File Information": {

                "File Name": file_name,

                "File Size": format_file_size(file_size),

                "Extension": extension,

                "Format": audio_format

            },

            "Audio Information": {

                "Duration": f"{duration:.2f} seconds",

                "Codec": codec,

                "Channels": channels,

                "Sampling Rate": f"{sample_rate} Hz",

                "Bit Rate": (
                    f"{bitrate / 1000:.2f} kbps"
                    if bitrate
                    else "Not available"
                )

            },

            "Metadata": metadata

        }

        return result

    except Exception as e:

        return {
            "error": f"Error reading audio: {e}"
        }


def print_report(result):
    """
    Print audio metadata report.
    """

    if "error" in result:

        print("\nERROR:", result["error"])

        return

    print()

    print("=" * 40)

    print("       AUDIO METADATA REPORT")

    print("=" * 40)

    print("\nFILE INFORMATION")

    print("-" * 40)

    file_info = result["File Information"]

    for key, value in file_info.items():

        print(f"{key:<20}: {value}")

    print("\nAUDIO")

    print("-" * 40)

    audio_info = result["Audio Information"]

    for key, value in audio_info.items():

        print(f"{key:<20}: {value}")

    print("\nMETADATA")

    print("-" * 40)

    metadata = result["Metadata"]

    if metadata:

        for key, value in metadata.items():

            print(f"{key:<20}: {value}")

    else:

        print("No additional metadata available.")


if __name__ == "__main__":

    file_path = input(
        "\nEnter audio file path: "
    ).strip().strip('"')

    result = analyze_audio(file_path)

    print_report(result)