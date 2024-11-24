import os
from os.path import isdir


def split_up_args(collected_args: list[str]) -> list[str]:
    """
    Parses the obtained line converts the arguments being sent
    into a string list for easier handling
    """
    extracted_args: list[str] = []

    for arg in collected_args:
        args = [x.strip() for x in arg.split(",")]
        extracted_args.extend(args)

    return extracted_args


def collect_python_files(
    base_dir: str, to_ignore: list[str] = ["__init__.py", "__pycache__", "README.md"]
) -> list[str]:
    """
    Collects all python files found in a given path,
    performs automatically a recursive call in order
    to handle folders within folders
    """
    found_files = []

    for obj in os.listdir(base_dir):
        if obj in to_ignore:
            continue

        path = f"{base_dir}/{obj}"

        if isdir(path):
            found_files.extend(collect_python_files(path))

        else:
            found_files.append(path)

    return found_files
