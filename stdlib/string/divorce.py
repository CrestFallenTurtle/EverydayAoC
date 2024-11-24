from backend.log import error
from backend.variables import try_get_variable_value, get_variable_name


class Divorce:
    def __init__(self) -> None:
        self.function_name = "divorce"
        self.max_limit = 3  # Sets the max amount of parameters that the user can enter
        self.lower_limit = (
            3  # Sets the least amount of parameters needed for the function to work
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
        delimiter = arguments[2]

        value_a = str(try_get_variable_value(var_a, var_namespace))
        value_b = str(try_get_variable_value(var_b, var_namespace))
        delimiter = str(try_get_variable_value(delimiter, var_namespace))

        if value_b == var_b:
            error(f"No variable to store the finalized results was passed")

        var_b = get_variable_name(var_b)

        split = value_a.split(delimiter)

        var_namespace[var_b] = split
