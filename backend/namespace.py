import ast
import importlib

from backend.config import LIBS_LOCATION
from backend.log import debug, warning
from backend.tools import collect_python_files


def create_lib_namespace() -> dict[str, any]:
    """
    Looks in the 'stdlib' folder and dynamically creates a namespace,
    which is returned back to the program
    """
    namespace = {}

    for lib in collect_python_files(LIBS_LOCATION):
        lib = lib.replace("/", ".")

        debug(f"found library {lib}")

        # Ignore this assignment for now
        class_name = lib
        module_path = lib

        # Remove the ending .py trail since this will only cause issues
        if module_path.endswith(".py"):
            module_path = module_path.replace(".py", "")

        if class_name.endswith(".py"):
            class_name = class_name.replace(".py", "")

        # Converts, e.g. print to Print (which should be the class name)
        class_name = class_name.title()

        class_name = class_name.split(".")[-1]

        lib_class = getattr(importlib.import_module(f"{module_path}"), class_name)

        class_object = lib_class()

        namespace[class_object.function_name] = class_object

        debug(f"generated and added library {module_path} to the namespace")

    return namespace


def create_var_namespace(variables: list[str]) -> dict[str, any]:
    """
    Obtains the variables found during parsing,
    and constructs a "namespace" for them to exist
    and live their life until death.

    This namespace/retirement home is returned to the program
    """
    namespace = {}

    is_a_string = False
    for var in variables:
        # Obtain the variable
        var_name, var_value = var.split("=", maxsplit=1)

        var_name = var_name.strip()
        var_value = var_value.strip()

        if var_name in namespace.keys():
            warning(
                f"Variable '{var_name}' has already been defined, will overwrite it with a new entry"
            )

        # Remove unnecessary extra ""
        if var_value.startswith('"'):
            is_a_string = True
            var_value = var_value[1:]

        if var_value.endswith('"'):
            is_a_string = True
            var_value = var_value[:-1]

        # If the variable is an integer, then we should try to convert it
        if not is_a_string:
            try:
                int_var_value = int(var_value)
                var_value = int_var_value
            except ValueError:
                debug(f"Failed to convert {var_value} to integer")

        # Check if a list was entered
        try:
            if isinstance(ast.literal_eval(str(var_value)), list):
                var_value = ast.literal_eval(str(var_value))

            else:
                debug(
                    f"Failed to convert {var_value} to a list, assume it's not a list then"
                )
        except (SyntaxError, ValueError):
            debug(f"Failed to check if the variable, {var_name}, could be a list")

        debug(f"inserting var {var_name} with value {var_value} into the namespace")
        namespace[var_name] = var_value

    return namespace


def create_method_namespace(methods: list[str]) -> dict[str, any]:
    """
    Obtains the variables found during parsing,
    and constructs a "namespace" for them to exist
    and live their life until death.

    This namespace/retirement home is returned to the program
    """
    namespace = {}
    collect_method: bool = False
    method_name = ""
    method_gut: list[str] = []

    for method_line in methods:

        # If the line ends with, ":", then it's the methods name
        if method_line.endswith(":"):

            if collect_method:
                namespace[method_name] = method_gut
                # Reset the gut
                method_gut = []

            method_name = method_line[:-1]
            collect_method = True
            continue

        if collect_method:
            method_gut.append(method_line)

    namespace[method_name] = method_gut

    return namespace
