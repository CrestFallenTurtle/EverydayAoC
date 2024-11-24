from backend.log import warning
from backend.variables import get_variable_name


class Obtain:

    def __init__(self) -> None:
        self.function_name = "obtain"

        self.max_limit = 1  # Sets the max amount of parameters that the user can enter
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

        targeted_variable = arguments[0]

        stripped_var_name = get_variable_name(targeted_variable)

        if stripped_var_name == targeted_variable:
            warning("The method did not obtain a variable to save the input in")

        var_namespace[stripped_var_name] = input(">> ")
