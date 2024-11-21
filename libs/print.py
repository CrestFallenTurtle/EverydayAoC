# Damn what is this guy printing...

class Print:
    """
    Implements basic output
    """

    def __init__(self) -> None:
        self.function_name = "print"

    def start(self, arguments:list[str]) -> None:
        """ main meat method each library """

        for value in arguments:
            print(value)