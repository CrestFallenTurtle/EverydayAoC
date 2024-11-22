import argparse
from backend.parser import parse_file, parse_variable_section, parse_main_loop, parse_end_loop, parse_method_section, identify_sections
from backend.runner import execute_converted_code
from backend.log import setup_log, error
from backend.namespace import create_lib_namespace, create_var_namespace

setup_log()

def main(file_input:str) -> None:
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
        #methods: list[str] = parse_method_section(file_gut)

        var_namespace = create_var_namespace(variables)

        main_loop: list[str] = parse_main_loop(file_gut)
        end_loop: list[str] = parse_end_loop(file_gut)


        # Time to execute our loops
        for loop in [main_loop, end_loop]:
            execute_converted_code(lib_namespace, loop, var_namespace)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="aaaaaaah every day I wake up 😭😭😭😭")

    parser.add_argument("--file", "-file", help="File to parse and execute", required=True)

    parsed_args = parser.parse_args()

    main(parsed_args.file)