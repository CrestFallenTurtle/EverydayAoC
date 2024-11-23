from backend.log import error, warning


class Obtain:

    def __init__(self) -> None:
        self.function_name = "obtain"

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:
        """main meat method each library"""

        if len(arguments) != 1:
            error(
                f"The wrong amount of arguments where sent in, expected one, got {len(arguments)}"
            )

        targeted_variable = arguments[0]

        if not targeted_variable.startswith("$"):
            warning("The method did not obtain a variable to save the input in")

        targeted_variable = targeted_variable[1:]

        var_namespace[targeted_variable] = input(">> ")
