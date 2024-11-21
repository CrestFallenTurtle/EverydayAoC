from os.path import exists

def parse_file(file_path:str) -> list[str]:
    """ 
        Reads the provided file,  
    
    """
    if not exists(file_path):
        # Raise error
        pass 

    guts = open(file_path, "r").readlines()

    print(guts)


def parse_variable_section(file_gut:str) -> list[str]:
    """ Parses the input file and definies every declared variable """

    pattern = ""