import json
import os
import subprocess
import sys
from os.path import isdir

IGNORE_FILES = ["input.pyass"]
EXPECTED_OUTPUT = "test/example/expected_output.json"


def collect_example_files(base_dir: str = "example") -> list[str]:
    """
    Collects all example files
    """
    found_files = []

    for obj in os.listdir(base_dir):

        if obj in IGNORE_FILES:
            continue

        path = f"{base_dir}/{obj}"

        if isdir(path):
            found_files.extend(collect_example_files(path))

        else:
            found_files.append(path)

    return found_files


def main() -> None:
    example_files = collect_example_files()
    expected_output: dict = {}

    with open(EXPECTED_OUTPUT) as handler:
        expected_output: dict = json.load(handler)

    for file in example_files:

        if file not in expected_output.keys():
            sys.exit(
                f"Found an example file which there was no expected output from, {file}"
            )

        try:
            result = str(subprocess.check_output(["python", "main.py", "-f", file]))
            expected = str(expected_output[file])

            if expected != result:
                sys.exit(f"Example file failed, expected: {expected}, got: {result}")

            print(f"Done checking example file {file}")

        except (subprocess.CalledProcessError, AttributeError) as err:
            sys.exit(f"File {file} failed with error msg: {err}")


if __name__ == "__main__":
    main()
