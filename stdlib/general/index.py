from backend.log import error
from backend.variables import is_variable, try_get_variable_value, get_variable_name


class Index:
    def __init__(self) -> None:
        self.function_name = "index"
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

        src_var = arguments[0]
        index = arguments[1]
        result_var = arguments[2]

        if not is_variable(result_var):
            error(f"No variable to store the finalized results was passed")

        var_result = get_variable_name(result_var)

        # Try to obtain a value
        src_var = try_get_variable_value(src_var, var_namespace)
        index = try_get_variable_value(index, var_namespace)

        try:
            index = int(index)

            # If it's an int, then just make it a string
            if isinstance(src_var, int):
                src_var = str(src_var)

            var_namespace[var_result] = src_var[index]

        except ValueError as err:
            error(
                f"Failed to convert one or more of the provided arguments into an integer\n{err}"
            )

        except IndexError as err:
            error(
                f"The requested index lies out of bounds given the length of the source variable\n{err}"
            )