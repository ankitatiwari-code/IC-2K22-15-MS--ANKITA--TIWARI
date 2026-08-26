import subprocess
import json
import os
import sys


def analyze_video(video_path):

    # Check file
    if not os.path.exists(video_path):
        print("ERROR: Video file not found!")
        print(video_path)
        return

    try:

        # Run FFprobe
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

        # Check FFprobe error
        if result.returncode != 0:
            print("ERROR: FFprobe failed")
            print(result.stderr)
            return

        # Convert JSON output
        data = json.loads(result.stdout)

        format_info = data.get("format", {})
        streams = data.get("streams", [])

        # ==================================================
        # VIDEO ANALYSIS REPORT
        # ==================================================

        print("\n" + "=" * 60)
        print("             VIDEO ANALYSIS REPORT")
        print("=" * 60)

        # ==================================================
        # FILE INFORMATION
        # ==================================================

        print("\nFILE INFORMATION")
        print("-" * 60)

        print("File Name     :", os.path.basename(video_path))
        print("File Path     :", os.path.abspath(video_path))

        file_size = os.path.getsize(video_path)

        print(
            "File Size     :",
            round(file_size / (1024 * 1024), 2),
            "MB"
        )

        print(
            "Format        :",
            format_info.get("format_name", "N/A")
        )

        print(
            "Format Details:",
            format_info.get(
                "format_long_name",
                "N/A"
            )
        )

        # ==================================================
        # DURATION
        # ==================================================

        print("\nDURATION")
        print("-" * 60)

        duration = format_info.get("duration")

        if duration:

            duration = float(duration)

            hours = int(duration // 3600)

            minutes = int(
                (duration % 3600) // 60
            )

            seconds = int(
                duration % 60
            )

            print(
                "Duration      :",
                f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            )

            print(
                "Duration Sec   :",
                round(duration, 2)
            )

        else:
            print("Duration      : N/A")

        # ==================================================
        # CONTAINER METADATA
        # ==================================================

        print("\nCONTAINER METADATA")
        print("-" * 60)

        print(
            "Format Name   :",
            format_info.get(
                "format_name",
                "N/A"
            )
        )

        print(
            "Start Time    :",
            format_info.get(
                "start_time",
                "N/A"
            )
        )

        print(
            "Overall Bitrate:",
            format_info.get(
                "bit_rate",
                "N/A"
            )
        )

        # ==================================================
        # EMBEDDED METADATA / TAGS
        # ==================================================

        print("\nEMBEDDED METADATA")
        print("-" * 60)

        tags = format_info.get("tags", {})

        if tags:

            for key, value in tags.items():

                print(
                    f"{key:20} : {value}"
                )

        else:

            print(
                "No embedded metadata found."
            )

        # ==================================================
        # FIND VIDEO AND AUDIO STREAMS
        # ==================================================

        video_streams = []

        audio_streams = []

        for stream in streams:

            codec_type = stream.get(
                "codec_type"
            )

            if codec_type == "video":
                video_streams.append(stream)

            elif codec_type == "audio":
                audio_streams.append(stream)

        # ==================================================
        # VIDEO INFORMATION
        # ==================================================

        print("\nVIDEO INFORMATION")
        print("-" * 60)

        print(
            "Video Streams :",
            len(video_streams)
        )

        for index, stream in enumerate(
            video_streams,
            start=1
        ):

            print(
                f"\n--- Video Stream {index} ---"
            )

            print(
                "Codec         :",
                stream.get(
                    "codec_name",
                    "N/A"
                )
            )

            print(
                "Codec Details :",
                stream.get(
                    "codec_long_name",
                    "N/A"
                )
            )

            print(
                "Profile       :",
                stream.get(
                    "profile",
                    "N/A"
                )
            )

            width = stream.get("width")
            height = stream.get("height")

            print(
                "Width         :",
                width,
                "pixels"
            )

            print(
                "Height        :",
                height,
                "pixels"
            )

            if width and height:

                print(
                    "Resolution    :",
                    f"{width} x {height}"
                )

                aspect_ratio = width / height

                print(
                    "Aspect Ratio  :",
                    round(
                        aspect_ratio,
                        2
                    )
                )

            # FPS
            frame_rate = stream.get(
                "r_frame_rate"
            )

            if frame_rate and "/" in frame_rate:

                parts = frame_rate.split("/")

                numerator = float(parts[0])
                denominator = float(parts[1])

                if denominator != 0:

                    fps = (
                        numerator /
                        denominator
                    )

                    print(
                        "Frame Rate    :",
                        round(fps, 2),
                        "FPS"
                    )

            print(
                "Pixel Format  :",
                stream.get(
                    "pix_fmt",
                    "N/A"
                )
            )

            print(
                "Frame Count   :",
                stream.get(
                    "nb_frames",
                    "N/A"
                )
            )

            print(
                "Video Bitrate :",
                stream.get(
                    "bit_rate",
                    "N/A"
                )
            )

            print(
                "Time Base     :",
                stream.get(
                    "time_base",
                    "N/A"
                )
            )

            language = stream.get(
                "tags",
                {}
            ).get(
                "language",
                "N/A"
            )

            print(
                "Language      :",
                language
            )

        # ==================================================
        # AUDIO INFORMATION
        # ==================================================

        print("\nAUDIO INFORMATION")
        print("-" * 60)

        print(
            "Audio Streams :",
            len(audio_streams)
        )

        for index, stream in enumerate(
            audio_streams,
            start=1
        ):

            print(
                f"\n--- Audio Stream {index} ---"
            )

            print(
                "Codec         :",
                stream.get(
                    "codec_name",
                    "N/A"
                )
            )

            print(
                "Codec Details :",
                stream.get(
                    "codec_long_name",
                    "N/A"
                )
            )

            print(
                "Sample Rate   :",
                stream.get(
                    "sample_rate",
                    "N/A"
                ),
                "Hz"
            )

            print(
                "Channels      :",
                stream.get(
                    "channels",
                    "N/A"
                )
            )

            print(
                "Channel Layout:",
                stream.get(
                    "channel_layout",
                    "N/A"
                )
            )

            print(
                "Audio Bitrate :",
                stream.get(
                    "bit_rate",
                    "N/A"
                )
            )

            language = stream.get(
                "tags",
                {}
            ).get(
                "language",
                "N/A"
            )

            print(
                "Language      :",
                language
            )

        # ==================================================
        # STREAM SUMMARY
        # ==================================================

        print("\nSTREAM SUMMARY")
        print("-" * 60)

        print(
            "Total Streams :",
            len(streams)
        )

        print(
            "Video Streams :",
            len(video_streams)
        )

        print(
            "Audio Streams :",
            len(audio_streams)
        )

        # ==================================================
        # OTHER STREAMS
        # ==================================================

        other_streams = []

        for stream in streams:

            codec_type = stream.get(
                "codec_type"
            )

            if codec_type not in [
                "video",
                "audio"
            ]:

                other_streams.append(
                    stream
                )

        print(
            "Other Streams :",
            len(other_streams)
        )

        for stream in other_streams:

            print(
                "Other Type    :",
                stream.get(
                    "codec_type",
                    "N/A"
                )
            )

        # ==================================================
        # END
        # ==================================================

        print("\n" + "=" * 60)
        print("          ANALYSIS COMPLETED")
        print("=" * 60)

    except FileNotFoundError:

        print(
            "\nERROR: FFprobe was not found!"
        )

        print(
            "Make sure FFmpeg is installed "
            "and added to PATH."
        )

    except json.JSONDecodeError:

        print(
            "\nERROR: Could not read FFprobe JSON."
        )

    except Exception as e:

        print(
            "\nERROR:",
            str(e)
        )


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

    analyze_video(video_file)