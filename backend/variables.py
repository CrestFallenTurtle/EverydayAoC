from backend.log import warning


def obtain_variable_value(variable: str, var_namespace: dict[str, any]) -> any:
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
