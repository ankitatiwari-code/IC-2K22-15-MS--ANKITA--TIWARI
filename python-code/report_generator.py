import json
import os
from datetime import datetime


def create_report(file_path, file_type, analysis_result):
    """Create a complete multimedia analysis report."""

    file_name = os.path.basename(file_path)

    file_size_bytes = os.path.getsize(file_path)
    file_size_mb = file_size_bytes / (1024 * 1024)

    report = {
        "report_information": {
            "generated_on": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "file_name": file_name,
            "file_type": file_type,
            "file_size": f"{file_size_mb:.2f} MB"
        },

        "analysis": analysis_result
    }

    return report


def save_report(report, output_file="reports/report.json"):
    """Save report as JSON."""

    folder = os.path.dirname(output_file)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\n======================================")
    print("          REPORT GENERATED")
    print("======================================")

    print(
        "Report saved at:"
    )

    print(
        os.path.abspath(output_file)
    )


def display_report(report):
    """Display report in readable format."""

    print("\n======================================")
    print("       CONSOLIDATED ANALYSIS REPORT")
    print("======================================")

    information = report.get(
        "report_information",
        {}
    )

    print("\nREPORT INFORMATION")
    print("--------------------------------------")

    print(
        f"File Name       : "
        f"{information.get('file_name', 'N/A')}"
    )

    print(
        f"File Type       : "
        f"{information.get('file_type', 'N/A')}"
    )

    print(
        f"File Size       : "
        f"{information.get('file_size', 'N/A')}"
    )

    print(
        f"Generated On    : "
        f"{information.get('generated_on', 'N/A')}"
    )

    print("\nANALYSIS")
    print("--------------------------------------")

    analysis = report.get(
        "analysis",
        {}
    )

    display_dictionary(analysis)


def display_dictionary(data, indent=0):
    """Display dictionary recursively."""

    if isinstance(data, dict):

        for key, value in data.items():

            formatted_key = str(
                key
            ).replace(
                "_",
                " "
            ).title()

            if isinstance(value, dict):

                print(
                    " " * indent +
                    f"\n{formatted_key}"
                )

                print(
                    " " * indent +
                    "-" * 35
                )

                display_dictionary(
                    value,
                    indent + 4
                )

            elif isinstance(value, list):

                print(
                    " " * indent +
                    f"{formatted_key}:"
                )

                for item in value:

                    if isinstance(item, dict):

                        display_dictionary(
                            item,
                            indent + 4
                        )

                    else:

                        print(
                            " " * (indent + 4) +
                            f"- {item}"
                        )

            else:

                print(
                    " " * indent +
                    f"{formatted_key:<20}: {value}"
                )

    else:

        print(
            " " * indent +
            str(data)
        )