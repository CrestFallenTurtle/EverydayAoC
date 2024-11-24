from backend.log import error, debug
from backend.tools import split_up_args


def execute_converted_code(
    gut: list[str],
    var_namespace: dict[str, any],
    method_namespace: dict[str, any],
    lib_namespace: dict[str, any],
) -> None:
    """
    Looks at the pyAss code in the loop list, and executes the corresponding python code
    """
    for line in gut:
        # Extract the function and args (hopefully)
        function, *collected_args = line.split(" ", maxsplit=1)

        # display_variables_in_memory(var_namespace)
        args = split_up_args(collected_args, var_namespace)

        # Goes through everything defined in the namespace, and find the called function
        found_function = False

        for lib_function in lib_namespace.keys():

            # And if the called function matches a builtin function
            # then we call it and pass all the arguments provided
            if lib_function.lower() == function.lower():
                class_object = lib_namespace[lib_function]

                max_args = class_object.max_limit
                low_args = class_object.lower_limit

                debug(
                    f"Method {lib_function}, defined MAX_ARGS={max_args} and LOW_ARGS={low_args}"
                )

                debug(f"The arguments {args} was sent to method {lib_function}")

                # The max args sets the MAXIMUM amount of allowed arguments to enter
                # and -1 disables this
                if max_args != -1 and max_args < len(args):
                    error(
                        f"The wrong amount of arguments where sent in to method {lib_function}, expected {max_args}, got {len(args)}"
                    )

                # The low args sets the LOWEST amount of allowed arguments to enter
                # and -1 disables this. Aka, "this many arguments are needed to run the function"
                if low_args != -1 and low_args > len(args):
                    error(
                        f"The wrong amount of arguments where sent in to method {lib_function}, required {low_args}, got {len(args)}"
                    )

                class_object.start(args, var_namespace, method_namespace, lib_namespace)
                found_function = True

        if not found_function:
            error(f"The called function '{function}', was not found")
