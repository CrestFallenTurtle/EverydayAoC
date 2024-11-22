# Damn what is this guy printing...
from backend.variables import obtain_variable_value


class Print:
    """
    Implements basic output
    """

    def __init__(self) -> None:
        self.function_name = "print"

    def start(self, arguments:list[str], var_namespace:dict[str, any]) -> None:
        """ main meat method each library """

        for value in arguments:
            if value.startswith("$"):
                value = obtain_variable_value(value, var_namespace)

            else:
                # Remove unnecessary extra ""
                if value.startswith('"'):
                    value = value[1:]

                if value.endswith('"'):
                    value = value[:-1]

            print(value)