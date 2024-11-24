from backend.log import error
from backend.variables import try_get_variable_value, get_variable_name


class Decrement:

    def __init__(self) -> None:
        self.function_name = "dec"
        self.max_limit = -1  # Sets the max amount of parameters that the user can enter
        self.lower_limit = (
            1  # Sets the least amount of parameters needed for the function to work
        )

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:

        # Probably overkill, but create a namespace
        for arg in arguments:
            var_value = try_get_variable_value(arg, var_namespace)
            var_name = get_variable_name(arg)

            try:
                var_namespace[var_name] = int(var_value) - 1

            except ValueError as err:
                error(
                    f"Failed to convert value of variable {var_name} into an integer\n{err}"
                )
