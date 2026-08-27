from PIL import Image, ExifTags
import os
import sys


def format_file_size(size):
    """Convert bytes into KB/MB."""
    if size < 1024:
        return f"{size} Bytes"
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size / (1024 * 1024):.2f} MB"


def get_exif_data(image):
    """Extract EXIF metadata from the image."""
    exif_data = {}

    try:
        exif = image.getexif()

        if not exif:
            return exif_data

        for tag_id, value in exif.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            exif_data[tag] = value

    except Exception:
        pass

    return exif_data


def analyze_image(image_path):

    # Check if file exists
    if not os.path.isfile(image_path):
        print("Error: File not found.")
        return

    # Supported formats
    supported_formats = {
        ".jpg", ".jpeg", ".png",
        ".tiff", ".tif",
        ".webp", ".bmp"
    }

    extension = os.path.splitext(image_path)[1].lower()

    if extension not in supported_formats:
        print("Error: Unsupported image format.")
        print("Supported formats: JPG, JPEG, PNG, TIFF, WEBP, BMP")
        return

    try:
        image = Image.open(image_path)

        file_name = os.path.basename(image_path)
        file_size = os.path.getsize(image_path)
        file_format = image.format
        width, height = image.size
        color_mode = image.mode

        # Resolution
        dpi = image.info.get("dpi")

        if dpi:
            resolution = f"{dpi[0]:.0f} x {dpi[1]:.0f} DPI"
        else:
            resolution = "Not available"

        # EXIF
        exif_data = get_exif_data(image)

        camera = exif_data.get("Model", "Not available")

        date_taken = (
            exif_data.get("DateTimeOriginal")
            or exif_data.get("DateTime")
            or "Not available"
        )

        orientation = exif_data.get("Orientation", "Not available")

        # Print report
        print("=" * 32)
        print("IMAGE METADATA REPORT")
        print("=" * 32)

        print()
        print(f"File Name       : {file_name}")
        print(f"File Size       : {format_file_size(file_size)}")
        print(f"File Format     : {file_format}")
        print(f"Width           : {width} pixels")
        print(f"Height          : {height} pixels")
        print(f"Resolution      : {resolution}")
        print(f"Color Mode      : {color_mode}")

        print()
        print("EXIF Metadata")
        print("-" * 31)

        print(f"Camera          : {camera}")
        print(f"Date Taken      : {date_taken}")
        print(f"Orientation     : {orientation}")

        # Print remaining EXIF metadata
        displayed_tags = {
            "Model",
            "DateTimeOriginal",
            "DateTime",
            "Orientation"
        }

        for tag, value in exif_data.items():

            if tag not in displayed_tags:

                # Avoid printing extremely large/unreadable values
                value_str = str(value)

                if len(value_str) > 100:
                    value_str = value_str[:100] + "..."

                print(f"{tag:<16}: {value_str}")

        image.close()

    except Exception as e:
        print(f"Error reading image: {e}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python image_analyzer.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

   def analyze_image(file_path):
    # image analysis code
    return result