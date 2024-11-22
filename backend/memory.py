def display_variables_in_memory(var_namespace: dict[str, any]) -> None:

    print("# Variable Name ## Variable Value #")
    for name, value in var_namespace.items():
        print(f"#  {name} ## {value} #")
