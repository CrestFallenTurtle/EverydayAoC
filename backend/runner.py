from backend.log import error
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
                class_object.start(args, var_namespace, method_namespace, lib_namespace)
                found_function = True

        if not found_function:
            error(f"The called function '{function}', was not found")
