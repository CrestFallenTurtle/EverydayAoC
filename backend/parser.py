from os.path import exists

from backend.config import (
    COMMENTS,
    END_LOOP_SECTION,
    MAIN_LOOP_SECTION,
    METHOD_START_SECTION,
    OPTIONAL_SECTIONS,
    REQUIRED_SECTIONS,
    VARIABLE_START_SECTION,
)
from backend.log import warning


def parse_file(file_path: str) -> list[str]:
    """
    Reads the provided file, removes newlines, tabs and empty lines,
    and returns the parsed results
    """
    extracted_fields: list[str] = []
    if not exists(file_path):
        raise Exception(f"failed to find file '{file_path}'")

    guts = open(file_path, "r").readlines()

    for line in guts:
        # Skip the current line if it starts with a #
        if line.startswith(COMMENTS):
            continue

        # Identify if there is a comment within the code, and if that is the case removes it
        comment_location = line.find(COMMENTS)
        if comment_location != -1:
            line = line[:comment_location]

        # Removes newlines and tabs
        line: str = line.strip()

        # Removes unnecessary lines
        if not line or line == " ":
            continue

        extracted_fields.append(line)

    return extracted_fields


def identify_sections(file_gut: list[str]) -> None:
    """
    Goes through the file gut and ...
        - Raises an exception if a required section is not identified
        - Logs a warning if an optional section is not identified
    """

    for section in REQUIRED_SECTIONS.keys():
        if section not in file_gut:
            raise Exception(f"The required section, {section}, was not found")

    for section in OPTIONAL_SECTIONS.keys():
        if section not in file_gut:
            warning(f"An optional section, {section}, was not found")


def parse_variable_section(file_gut: list[str]) -> list[str]:
    """
    Parses the input file and identifies every defined variable,
    these are returned back to the calling method
    """
    declared_variables: list[str] = []
    collect_vars: bool = False

    for line in file_gut:
        # Start collecting variables
        if line == VARIABLE_START_SECTION:
            collect_vars = True
            continue

        # Stop collecting variables if we hit this section
        if line in [METHOD_START_SECTION, MAIN_LOOP_SECTION, END_LOOP_SECTION]:
            collect_vars = False
            continue

        if collect_vars:
            declared_variables.append(line)

    return declared_variables


def parse_method_section(file_gut: list[str]) -> list[str]:
    """
    Parses the input file and identifies every defined method,
    these are returned back to the calling method
    """
    declared_methods: list[str] = []
    collect_meth: bool = False

    for line in file_gut:
        # Start collecting variables
        if line == METHOD_START_SECTION:
            collect_meth = True
            continue

        # Stop collecting variables if we hit this section
        if line in [VARIABLE_START_SECTION, MAIN_LOOP_SECTION, END_LOOP_SECTION]:
            collect_meth = False
            continue

        if collect_meth:
            declared_methods.append(line)

    return declared_methods


def parse_main_loop(file_gut: list[str]) -> list[str]:
    """
    Parses the input file and creates the main loop of the program,
    the contents of the main loop is returned back to the calling method
    """
    main_loop_gut: list[str] = []
    collect: bool = False

    for line in file_gut:
        if line == MAIN_LOOP_SECTION:
            collect = True
            continue

        if line in [VARIABLE_START_SECTION, METHOD_START_SECTION, END_LOOP_SECTION]:
            collect = False
            continue

        if collect:
            main_loop_gut.append(line)

    return main_loop_gut


def parse_end_loop(file_gut: list[str]) -> list[str]:
    """
    Parses the input file and creates the end loop of the program,
    the contents of the end loop is returned back to the calling method
    """
    end_loop_gut: list[str] = []
    collect: bool = False

    for line in file_gut:
        if line == END_LOOP_SECTION:
            collect = True
            continue

        if line in [VARIABLE_START_SECTION, METHOD_START_SECTION, MAIN_LOOP_SECTION]:
            collect = False
            continue

        if collect:
            end_loop_gut.append(line)

    return end_loop_gut
