import backend.parser
import tempfile


def test_parse_file() -> None:
    gut = """
WAKE UP

A=10
B=20
C="Otto Von Bismarck"

PIECE OF SHIT

FUCK THIS SHIT
"""
    with tempfile.NamedTemporaryFile() as tmp_file:
        tmp_file.write(gut)
        parsed_file = backend.parser.parse_file(tmp_file.name)

    
    print(parsed_file)


def test_parse_variable_section() -> None:
    parsed_file=[]

    parsed_variables = backend.parser.parse_variable_section(parsed_file)