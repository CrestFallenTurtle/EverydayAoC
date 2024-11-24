from backend.log import warning


def get_variable_name(
    potential_var: str,
) -> str:
    """
    Looks at the obtained parameter, and checks if it's a variable
    or not, if it's a variable, than the $-sign is removed and the rest is returned
    if it's not a variable, than the string is returned as it is
    """

    if potential_var.startswith("$"):
        potential_var = potential_var[1:]

    return potential_var


def try_get_variable_value(
    potential_var: str,
    var_namespace: dict[str, any],
) -> str | int | list:
    """
    Looks at the obtained parameter, and checks if it's a variable
    or not, if it's a variable, than the value of the variable is returned
    if it's not a variable, than the string is returned as it is
    """
    to_return: str | int | list = potential_var
    modified_var = get_variable_name(potential_var)

    # Did the name change? If so, then we can assume it to be a variable
    if modified_var != potential_var:
        if modified_var not in var_namespace.keys():
            warning(
                f"Variable {modified_var} was called but it has never been declared"
            )

        else:
            # Replace the value with what we have in our namespace,
            # this should effectively convert, $str -> "Hello World"
            to_return = var_namespace[modified_var]

    return to_return
