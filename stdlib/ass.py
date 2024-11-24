from backend.log import warning, debug
from backend.variables import try_get_variable_value


class Ass:
    """
    Implements basic output
    """

    def __init__(self) -> None:
        self.function_name = "ass"
        self.max_limit = -1  # Sets the max amount of parameters that the user can enter
        self.lower_limit = 2 # Sets the least amount of parameters needed for the function to work

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:
        """main meat method each library"""

        value = arguments[0]
        variables = arguments[1:]

        # If the value is a variable, let us obtain it
        value = try_get_variable_value(value, var_namespace)

        for var in variables:
            # Did the user try to assign a value to something that is not a variable
            if not var.startswith("$"):
                debug("What is this user thinking")
                warning(f"Instead of a variable, a value was passed in. Thus shall be ignored")
                continue

            var = var[1:]

            # Insert the new value
            var_namespace[var] = value