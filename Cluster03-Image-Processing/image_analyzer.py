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
    """Analyze image and return metadata."""

    # Check if file exists
    if not os.path.isfile(image_path):
        return {
            "error": "File not found"
        }

    # Supported formats
    supported_formats = {
        ".jpg",
        ".jpeg",
        ".png",
        ".tiff",
        ".tif",
        ".webp",
        ".bmp"
    }

    extension = os.path.splitext(image_path)[1].lower()

    if extension not in supported_formats:
        return {
            "error": "Unsupported image format"
        }

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

        # EXIF metadata
        exif_data = get_exif_data(image)

        camera = exif_data.get(
            "Model",
            "Not available"
        )

        date_taken = (
            exif_data.get("DateTimeOriginal")
            or exif_data.get("DateTime")
            or "Not available"
        )

        orientation = exif_data.get(
            "Orientation",
            "Not available"
        )

        # Create result dictionary
        result = {

            "File Information": {
                "File Name": file_name,
                "File Size": format_file_size(file_size),
                "File Format": file_format,
                "Extension": extension
            },

            "Image Information": {
                "Width": f"{width} pixels",
                "Height": f"{height} pixels",
                "Resolution": resolution,
                "Color Mode": color_mode
            },

            "EXIF Metadata": {
                "Camera": camera,
                "Date Taken": date_taken,
                "Orientation": orientation
            },

            "Other Metadata": {}
        }

        # Add remaining EXIF metadata
        displayed_tags = {
            "Model",
            "DateTimeOriginal",
            "DateTime",
            "Orientation"
        }

        for tag, value in exif_data.items():

            if tag not in displayed_tags:

                value_str = str(value)

                # Avoid extremely large values
                if len(value_str) > 100:
                    value_str = value_str[:100] + "..."

                result["Other Metadata"][tag] = value_str

        image.close()

        return result

    except Exception as e:

        return {
            "error": f"Error reading image: {e}"
        }


def print_report(result):
    """Print image metadata report."""

    if "error" in result:
        print("\nERROR:", result["error"])
        return

    print()
    print("=" * 40)
    print("       IMAGE METADATA REPORT")
    print("=" * 40)

    print("\nFILE INFORMATION")
    print("-" * 40)

    file_info = result["File Information"]

    for key, value in file_info.items():
        print(f"{key:<18}: {value}")

    print("\nIMAGE")
    print("-" * 40)

    image_info = result["Image Information"]

    for key, value in image_info.items():
        print(f"{key:<18}: {value}")

    print("\nEXIF METADATA")
    print("-" * 40)

    exif_info = result["EXIF Metadata"]

    for key, value in exif_info.items():
        print(f"{key:<18}: {value}")

    print("\nOTHER METADATA")
    print("-" * 40)

    other_metadata = result["Other Metadata"]

    if other_metadata:

        for key, value in other_metadata.items():
            print(f"{key:<18}: {value}")

    else:
        print("No additional EXIF metadata available.")


if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage:")
        print("python image_analyzer.py <image_path>")

        sys.exit(1)

    image_path = sys.argv[1]

    result = analyze_image(image_path)

    print_report(result)