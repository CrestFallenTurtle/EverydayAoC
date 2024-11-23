from backend.log import error
from backend.variables import obtain_variable_value


class Bitwise_Not:

    def __init__(self) -> None:
        self.function_name = "bnot"

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:

        if len(arguments) != 2:
            error(
                f"The wrong amount of arguments where sent in, expected two, got {len(arguments)}"
            )

        namespace = {}

        # Probably overkill, but create a namespace
        for arg in arguments:
            if arg.startswith("$"):

                # Remove the dollar sign
                var_value = obtain_variable_value(arg, var_namespace)
                arg = arg[1:]

                namespace[arg] = var_value

            else:
                namespace[arg] = arg

        try:
            # This is so fucking stupid
            a = int(namespace[list(namespace.keys())[0]])

            resulting_var = list(namespace.keys())[1]
            var_namespace[resulting_var] = ~a

        except ValueError as err:
            error(
                f"Failed to convert one or more of the provided arguments into an integer\n{err}"
            )
