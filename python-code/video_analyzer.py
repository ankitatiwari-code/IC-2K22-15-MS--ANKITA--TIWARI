import subprocess
import json
import os
import sys


def format_file_size(size):
    """Convert bytes into a readable file size."""

    if size < 1024:
        return f"{size} Bytes"

    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"

    else:
        return f"{size / (1024 * 1024):.2f} MB"


def format_bitrate(bitrate):
    """Convert bitrate into kbps."""

    if not bitrate:
        return "N/A"

    try:
        return f"{float(bitrate) / 1000:.2f} kbps"

    except (ValueError, TypeError):
        return str(bitrate)


def format_duration(duration):
    """Convert seconds into HH:MM:SS."""

    if not duration:
        return "N/A"

    try:
        duration = float(duration)

        hours = int(duration // 3600)

        minutes = int(
            (duration % 3600) // 60
        )

        seconds = int(duration % 60)

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    except (ValueError, TypeError):
        return "N/A"


def get_fps(stream):
    """Calculate FPS from FFprobe frame rate."""

    frame_rate = stream.get("r_frame_rate")

    if frame_rate and "/" in frame_rate:

        try:
            numerator, denominator = frame_rate.split("/")

            numerator = float(numerator)
            denominator = float(denominator)

            if denominator != 0:

                return round(
                    numerator / denominator,
                    2
                )

        except (ValueError, ZeroDivisionError):
            pass

    return "N/A"


def analyze_video(video_path):
    """
    Analyze video using FFprobe and return
    metadata as a dictionary.
    """

    # ---------------------------------------------
    # Check file
    # ---------------------------------------------

    if not os.path.isfile(video_path):

        return {
            "error": "Video file not found",
            "file_path": video_path
        }

    try:

        # ---------------------------------------------
        # FFprobe command
        # ---------------------------------------------

        command = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            video_path
        ]

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # ---------------------------------------------
        # Check FFprobe error
        # ---------------------------------------------

        if result.returncode != 0:

            return {
                "error": "FFprobe failed",
                "details": result.stderr
            }

        # ---------------------------------------------
        # Convert JSON
        # ---------------------------------------------

        data = json.loads(result.stdout)

        format_info = data.get(
            "format",
            {}
        )

        streams = data.get(
            "streams",
            []
        )

        # ---------------------------------------------
        # File information
        # ---------------------------------------------

        file_name = os.path.basename(
            video_path
        )

        file_size = os.path.getsize(
            video_path
        )

        file_extension = os.path.splitext(
            video_path
        )[1].lower()

        # ---------------------------------------------
        # Duration
        # ---------------------------------------------

        duration = format_info.get(
            "duration"
        )

        duration_seconds = (
            round(float(duration), 2)
            if duration
            else "N/A"
        )

        # ---------------------------------------------
        # Find streams
        # ---------------------------------------------

        video_streams = []

        audio_streams = []

        other_streams = []

        for stream in streams:

            codec_type = stream.get(
                "codec_type"
            )

            if codec_type == "video":

                video_streams.append(stream)

            elif codec_type == "audio":

                audio_streams.append(stream)

            else:

                other_streams.append(stream)

        # ---------------------------------------------
        # VIDEO INFORMATION
        # ---------------------------------------------

        video_information = []

        for index, stream in enumerate(
            video_streams,
            start=1
        ):

            width = stream.get(
                "width"
            )

            height = stream.get(
                "height"
            )

            if width and height:

                resolution = (
                    f"{width} x {height}"
                )

                aspect_ratio = round(
                    width / height,
                    2
                )

            else:

                resolution = "N/A"

                aspect_ratio = "N/A"

            video_info = {

                "Stream": index,

                "Codec": stream.get(
                    "codec_name",
                    "N/A"
                ),

                "Codec Details": stream.get(
                    "codec_long_name",
                    "N/A"
                ),

                "Profile": stream.get(
                    "profile",
                    "N/A"
                ),

                "Width": width or "N/A",

                "Height": height or "N/A",

                "Resolution": resolution,

                "Aspect Ratio": aspect_ratio,

                "Frame Rate": get_fps(stream),

                "Pixel Format": stream.get(
                    "pix_fmt",
                    "N/A"
                ),

                "Frame Count": stream.get(
                    "nb_frames",
                    "N/A"
                ),

                "Bit Rate": format_bitrate(
                    stream.get("bit_rate")
                ),

                "Time Base": stream.get(
                    "time_base",
                    "N/A"
                ),

                "Language": stream.get(
                    "tags",
                    {}
                ).get(
                    "language",
                    "N/A"
                )
            }

            video_information.append(
                video_info
            )

        # ---------------------------------------------
        # AUDIO INFORMATION
        # ---------------------------------------------

        audio_information = []

        for index, stream in enumerate(
            audio_streams,
            start=1
        ):

            audio_info = {

                "Stream": index,

                "Codec": stream.get(
                    "codec_name",
                    "N/A"
                ),

                "Codec Details": stream.get(
                    "codec_long_name",
                    "N/A"
                ),

                "Sample Rate": (
                    f"{stream.get('sample_rate')} Hz"
                    if stream.get("sample_rate")
                    else "N/A"
                ),

                "Channels": stream.get(
                    "channels",
                    "N/A"
                ),

                "Channel Layout": stream.get(
                    "channel_layout",
                    "N/A"
                ),

                "Bit Rate": format_bitrate(
                    stream.get("bit_rate")
                ),

                "Language": stream.get(
                    "tags",
                    {}
                ).get(
                    "language",
                    "N/A"
                )
            }

            audio_information.append(
                audio_info
            )

        # ---------------------------------------------
        # Embedded metadata
        # ---------------------------------------------

        metadata = format_info.get(
            "tags",
            {}
        )

        metadata = {
            str(key): str(value)
            for key, value in metadata.items()
        }

        if not metadata:

            metadata = {
                "Information":
                "No embedded metadata found."
            }

        # ---------------------------------------------
        # Other streams
        # ---------------------------------------------

        other_stream_information = []

        for stream in other_streams:

            other_stream_information.append({

                "Type": stream.get(
                    "codec_type",
                    "N/A"
                ),

                "Codec": stream.get(
                    "codec_name",
                    "N/A"
                )
            })

        # ---------------------------------------------
        # FINAL RESULT
        # ---------------------------------------------

        result_data = {

            "File Information": {

                "File Name": file_name,

                "File Path": os.path.abspath(
                    video_path
                ),

                "File Size": format_file_size(
                    file_size
                ),

                "Extension": file_extension,

                "Container": format_info.get(
                    "format_name",
                    "N/A"
                ),

                "Format Details": format_info.get(
                    "format_long_name",
                    "N/A"
                )
            },

            "Duration": {

                "Formatted": format_duration(
                    duration
                ),

                "Seconds": duration_seconds
            },

            "Container Metadata": {

                "Format Name": format_info.get(
                    "format_name",
                    "N/A"
                ),

                "Start Time": format_info.get(
                    "start_time",
                    "N/A"
                ),

                "Overall Bitrate": format_bitrate(
                    format_info.get("bit_rate")
                )
            },

            "Video": {

                "Number of Streams": len(
                    video_information
                ),

                "Streams": video_information
            },

            "Audio": {

                "Number of Streams": len(
                    audio_information
                ),

                "Streams": audio_information
            },

            "Metadata": metadata,

            "Other Streams": {

                "Number of Streams": len(
                    other_stream_information
                ),

                "Streams": other_stream_information
            },

            "Stream Summary": {

                "Total Streams": len(streams),

                "Video Streams": len(
                    video_streams
                ),

                "Audio Streams": len(
                    audio_streams
                ),

                "Other Streams": len(
                    other_streams
                )
            }
        }

        return result_data

    except FileNotFoundError:

        return {
            "error":
            "FFprobe was not found. "
            "Make sure FFmpeg is installed "
            "and added to PATH."
        }

    except json.JSONDecodeError:

        return {
            "error":
            "Could not read FFprobe JSON."
        }

    except Exception as e:

        return {
            "error":
            f"Error analyzing video: {str(e)}"
        }


def print_report(result):
    """Print video analysis report."""

    if "error" in result:

        print("\nERROR:", result["error"])

        if "details" in result:
            print(result["details"])

        return

    print("\n" + "=" * 60)

    print(
        "             VIDEO ANALYSIS REPORT"
    )

    print("=" * 60)

    # ---------------------------------------------
    # FILE INFORMATION
    # ---------------------------------------------

    print("\nFILE INFORMATION")

    print("-" * 60)

    file_info = result["File Information"]

    for key, value in file_info.items():

        print(
            f"{key:<20}: {value}"
        )

    # ---------------------------------------------
    # DURATION
    # ---------------------------------------------

    print("\nDURATION")

    print("-" * 60)

    duration = result["Duration"]

    print(
        f"{'Duration':<20}: "
        f"{duration['Formatted']}"
    )

    print(
        f"{'Duration Seconds':<20}: "
        f"{duration['Seconds']}"
    )

    # ---------------------------------------------
    # CONTAINER METADATA
    # ---------------------------------------------

    print("\nCONTAINER METADATA")

    print("-" * 60)

    container = result[
        "Container Metadata"
    ]

    for key, value in container.items():

        print(
            f"{key:<20}: {value}"
        )

    # ---------------------------------------------
    # VIDEO
    # ---------------------------------------------

    print("\nVIDEO INFORMATION")

    print("-" * 60)

    video = result["Video"]

    print(
        f"{'Video Streams':<20}: "
        f"{video['Number of Streams']}"
    )

    for stream in video["Streams"]:

        print(
            f"\n--- Video Stream "
            f"{stream['Stream']} ---"
        )

        for key, value in stream.items():

            if key != "Stream":

                print(
                    f"{key:<20}: {value}"
                )

    # ---------------------------------------------
    # AUDIO
    # ---------------------------------------------

    print("\nAUDIO INFORMATION")

    print("-" * 60)

    audio = result["Audio"]

    print(
        f"{'Audio Streams':<20}: "
        f"{audio['Number of Streams']}"
    )

    for stream in audio["Streams"]:

        print(
            f"\n--- Audio Stream "
            f"{stream['Stream']} ---"
        )

        for key, value in stream.items():

            if key != "Stream":

                print(
                    f"{key:<20}: {value}"
                )

    # ---------------------------------------------
    # METADATA
    # ---------------------------------------------

    print("\nEMBEDDED METADATA")

    print("-" * 60)

    metadata = result["Metadata"]

    for key, value in metadata.items():

        print(
            f"{key:<20}: {value}"
        )

    # ---------------------------------------------
    # STREAM SUMMARY
    # ---------------------------------------------

    print("\nSTREAM SUMMARY")

    print("-" * 60)

    summary = result[
        "Stream Summary"
    ]

    for key, value in summary.items():

        print(
            f"{key:<20}: {value}"
        )

    # ---------------------------------------------
    # OTHER STREAMS
    # ---------------------------------------------

    other = result[
        "Other Streams"
    ]

    if other["Number of Streams"] > 0:

        print("\nOTHER STREAMS")

        print("-" * 60)

        for stream in other["Streams"]:

            print(
                f"Type            : "
                f"{stream['Type']}"
            )

            print(
                f"Codec           : "
                f"{stream['Codec']}"
            )

    print("\n" + "=" * 60)

    print(
        "          ANALYSIS COMPLETED"
    )

    print("=" * 60)


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    if len(sys.argv) < 2:

        print("\nUsage:")

        print(
            'python video_analyzer.py "video.mp4"'
        )

        sys.exit(1)

    video_file = sys.argv[1]

    result = analyze_video(
        video_file
    )

    print_report(result)