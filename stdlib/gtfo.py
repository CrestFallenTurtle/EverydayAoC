from backend.log import warning
from backend.runner import execute_converted_code


class Gtfo:
    def __init__(self) -> None:
        self.function_name = "gtfo"
        self.max_limit = -1  # Sets the max amount of parameters that the user can enter
        self.lower_limit = 2 # Sets the least amount of parameters needed for the function to work

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:
        """main meat method each library"""

        for meth_name in arguments:
            found_method = False

            for defined_meth_name, meth_gut in method_namespace.items():

                # We found the method we were looking for
                # so execute its content
                if meth_name == defined_meth_name:
                    found_method = True

                    execute_converted_code(
                        meth_gut, var_namespace, method_namespace, lib_namespace
                    )

            if not found_method:
                warning(f"Method {meth_name} was called but it has never been declared")
