from backend.log import error
from backend.variables import try_get_variable_value, is_variable, get_variable_name


class Strip:
    def __init__(self) -> None:
        self.function_name = "strip"
        self.max_limit = 2  # Sets the max amount of parameters that the user can enter
        self.lower_limit = (
            2  # Sets the least amount of parameters needed for the function to work
        )

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:

        var_a = arguments[0]
        var_b = arguments[1]

        if not is_variable(var_a):
            error(f"No variable to store the finalized results was passed")

        value_a = str(try_get_variable_value(var_a, var_namespace))
        value_b = str(try_get_variable_value(var_b, var_namespace))

        var_a = get_variable_name(var_a)

        var_namespace[var_a] = value_a.replace(value_b, "")