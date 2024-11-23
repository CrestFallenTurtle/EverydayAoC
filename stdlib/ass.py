from backend.log import error, warning, debug
from backend.variables import obtain_variable_value


class Ass:
    """
    Implements basic output
    """

    def __init__(self) -> None:
        self.function_name = "ass"

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:
        """main meat method each library"""

        if len(arguments) < 2:
            error(
                f"The wrong amount of arguments where sent in, expected least two, got {len(arguments)}"
            )

        value = arguments[0]
        variables = arguments[1:]

        # If the value is a variable, let us obtain it
        if value.startswith("$"):
            value = obtain_variable_value(value, var_namespace)

        for var in variables:
            # Did the user try to assign a value to something that is not a variable
            if not var.startswith("$"):
                debug("What is this user thinking")
                warning(f"Instead of a variable, a value was passed in. Thus shall be ignored")
                continue

            var = var[1:]

            # Insert the new value
            var_namespace[var] = value