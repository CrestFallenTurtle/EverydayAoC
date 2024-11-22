from backend.log import warning


def split_up_args(collected_args:list[str], var_namespace:dict[str, any]) -> list[str]:
    """
    Parses the obtained line converts the arguments being sent
    into a string list for easier handling, this will also handle any
    converting a variable call to its actual value
    """
    extracted_args: list[str] = []

    for arg in collected_args:
        args = [x.strip() for x in arg.split(",")]
        extracted_args.extend(args)

    return extracted_args


def obtain_variable_value(variable:str, var_namespace:dict[str, any]) -> any:
    """
    Looks up the variable name in the variable namespace, and returns it's assigned
    value if it's found.
    """

    if variable.startswith("$"):
        variable = variable[1:]

        if variable not in var_namespace.keys():
            warning(f"Variable {variable} was called but it has never been declared")
            return variable

        # Replace the value with what we have in our namespace,
        # this should effectively convert, $str -> "Hello World"
        variable = var_namespace[variable]

    return variable