def split_up_args(
    collected_args: list[str], var_namespace: dict[str, any]
) -> list[str]:
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
