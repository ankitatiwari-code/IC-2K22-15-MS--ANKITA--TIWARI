import os


# Supported image formats
IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".tif",
    ".webp"
}


# Supported audio formats
AUDIO_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".ogg",
    ".m4a",
    ".wma"
}


# Supported video formats
VIDEO_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".flv",
    ".webm",
    ".mpeg",
    ".mpg"
}


def validate_file(file_path):
    """
    Check whether the file exists and is a valid file.
    """

    if not file_path:
        return False

    if not os.path.exists(file_path):
        return False

    if not os.path.isfile(file_path):
        return False

    return True


def get_file_name(file_path):
    """
    Get only the file name.
    """

    return os.path.basename(file_path)


def get_file_size(file_path):
    """
    Get file size in bytes, KB and MB.
    """

    size_bytes = os.path.getsize(file_path)

    size_kb = size_bytes / 1024

    size_mb = size_kb / 1024

    return {
        "bytes": size_bytes,
        "KB": round(size_kb, 2),
        "MB": round(size_mb, 2)
    }


def get_file_extension(file_path):
    """
    Get file extension.
    """

    return os.path.splitext(
        file_path
    )[1].lower()


def identify_file_type(file_path):
    """
    Automatically identify file type.
    """

    extension = get_file_extension(
        file_path
    )

    if extension in IMAGE_EXTENSIONS:

        return "image"

    elif extension in AUDIO_EXTENSIONS:

        return "audio"

    elif extension in VIDEO_EXTENSIONS:

        return "video"

    else:

        return "unknown"


def get_file_information(file_path):
    """
    Get complete basic information about a file.
    """

    # Validate file
    if not validate_file(file_path):

        return {
            "valid": False,
            "error":
                "File does not exist or is not a valid file."
        }

    # Get size
    size = get_file_size(
        file_path
    )

    # Get extension
    extension = get_file_extension(
        file_path
    )

    # Get type
    file_type = identify_file_type(
        file_path
    )

    # Return information
    return {

        "valid": True,

        "file_name":
            get_file_name(file_path),

        "extension":
            extension,

        "file_type":
            file_type,

        "size_bytes":
            size["bytes"],

        "size_kb":
            size["KB"],

        "size_mb":
            size["MB"]
    }