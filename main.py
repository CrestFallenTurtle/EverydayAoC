import argparse

from backend.log import error, setup_log
from backend.namespace import (
    create_lib_namespace,
    create_var_namespace,
    create_method_namespace,
)
from backend.parser import (
    identify_sections,
    parse_end_loop,
    parse_file,
    parse_main_loop,
    parse_method_section,
    parse_variable_section,
)
from backend.runner import execute_converted_code

setup_log()


def main(file_input: str) -> None:
    file_gut: list[str] = []

    # Dynamically imports all our libraries and creates a namespace
    lib_namespace = create_lib_namespace()

    try:
        file_gut = parse_file(file_input)
        identify_sections(file_gut)

    except Exception as err:
        error(str(err))

    finally:
        variables: list[str] = parse_variable_section(file_gut)
        methods: list[str] = parse_method_section(file_gut)

        var_namespace = create_var_namespace(variables)
        method_namespace = create_method_namespace(methods)

        main_loop: list[str] = parse_main_loop(file_gut)
        end_loop: list[str] = parse_end_loop(file_gut)

        # Time to execute our loops
        for loop in [main_loop, end_loop]:
            execute_converted_code(loop, var_namespace, method_namespace, lib_namespace)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="aaaaaaah every day I wake up 😭😭😭😭")

    parser.add_argument(
        "--file", "-file", help="File to parse and execute", required=True
    )

    parsed_args = parser.parse_args()

    main(parsed_args.file)
