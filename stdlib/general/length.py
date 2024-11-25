from backend.log import error
from backend.variables import is_variable, try_get_variable_value, get_variable_name


class Length:
    def __init__(self) -> None:
        self.function_name = "length"
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
        var_result = arguments[1]

        if not is_variable(var_result):
            error(f"No variable to store the finalized results was passed")

        var_result = get_variable_name(var_result)

        # Try to obtain a value
        var_a = try_get_variable_value(var_a, var_namespace)

        # If it's an int, then just make it a string
        if isinstance(var_a, int):
            var_a = str(var_a)

        var_namespace[var_result] = len(var_a)