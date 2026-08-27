from file_utils import (
    validate_file,
    identify_file_type,
    get_file_information
)

from image_analyzer import analyze_image
from audio_analyzer import analyze_audio
from video_analyzer import analyze_video

from report_generator import (
    create_report,
    save_report,
    display_report
)


def main():

    print()
    print("=" * 50)
    print("       CONSOLIDATED MULTIMEDIA ANALYZER")
    print("=" * 50)

    # ---------------------------------------------
    # Get file path
    # ---------------------------------------------

    file_path = input(
        "\nEnter multimedia file path: "
    ).strip().strip('"')

    # ---------------------------------------------
    # Validate file
    # ---------------------------------------------

    if not validate_file(file_path):

        print("\nERROR: File does not exist!")

        return

    # ---------------------------------------------
    # Get file information
    # ---------------------------------------------

    file_information = get_file_information(
        file_path
    )

    print("\nFILE VALIDATED SUCCESSFULLY")
    print("--------------------------------------")

    print(
        f"File Name : "
        f"{file_information['file_name']}"
    )

    print(
        f"File Size : "
        f"{file_information['size_mb']} MB"
    )

    print(
        f"Extension : "
        f"{file_information['extension']}"
    )

    # ---------------------------------------------
    # Identify file type
    # ---------------------------------------------

    file_type = identify_file_type(
        file_path
    )

    print(
        f"File Type : "
        f"{file_type.upper()}"
    )

    # ---------------------------------------------
    # Select analyzer
    # ---------------------------------------------

    print("\n" + "=" * 50)

    if file_type == "image":

        print("Running IMAGE analyzer...")

        result = analyze_image(
            file_path
        )

    elif file_type == "audio":

        print("Running AUDIO analyzer...")

        result = analyze_audio(
            file_path
        )

    elif file_type == "video":

        print("Running VIDEO analyzer...")

        result = analyze_video(
            file_path
        )

    else:

        print(
            "ERROR: Unsupported file type."
        )

        return

    # ---------------------------------------------
    # Check analyzer result
    # ---------------------------------------------

    if not result:

        print(
            "\nERROR: Analyzer returned no result."
        )

        return

    if "error" in result:

        print(
            "\nERROR:",
            result["error"]
        )

        return

    # ---------------------------------------------
    # Create consolidated report
    # ---------------------------------------------

    report = create_report(
        file_path,
        file_type,
        result
    )

    # ---------------------------------------------
    # Display report
    # ---------------------------------------------

    display_report(
        report
    )

    # ---------------------------------------------
    # Save report
    # ---------------------------------------------

    save_report(
        report
    )


# ---------------------------------------------
# Program starts here
# ---------------------------------------------

if __name__ == "__main__":

    main()