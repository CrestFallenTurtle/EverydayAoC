# Damn what is this guy printing...
from backend.variables import try_get_variable_value


class Print:
    """
    Implements basic output
    """

    def __init__(self) -> None:
        self.function_name = "print"
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
        """main meat method each library"""

        for value in arguments:
            value = try_get_variable_value(value, var_namespace)

            if isinstance(value, str):
                # Remove unnecessary extra ""
                if value.startswith('"'):
                    value = value[1:]

                if value.endswith('"'):
                    value = value[:-1]

            print(value)
