import pytest

import backend.parser


@pytest.mark.skip("Annoying to test")
def test_parse_file() -> None:
    pass


@pytest.mark.skip("Annoying to test, and the method doesn't return anything to test")
def test_identify_sections() -> None:
    pass


def test_parse_variable_section() -> None:
    example_file = ["WAKE UP", "A = 20", "B = 30", "C = 40", "PIECE OF SHIT"]

    parsed = backend.parser.parse_variable_section(example_file)

    assert parsed == ["A = 20", "B = 30", "C = 40"]


def test_parse_method_section() -> None:
    example_file = [
        "EVERYDAY I WAKE UP",
        "foo:",
        "print $str",
        "add $a, $b, $c",
        "PIECE OF SHIT",
    ]

    parsed = backend.parser.parse_method_section(example_file)

    assert parsed == ["foo:", "print $str", "add $a, $b, $c"]


def test_parse_main_loop() -> None:
    example_file = [
        "PIECE OF SHIT",
        "gtfo foo, boo",
        "FUCK THIS SHIT",
    ]

    parsed = backend.parser.parse_main_loop(example_file)

    assert parsed == ["gtfo foo, boo"]


def test_parse_end_loop() -> None:
    example_file = [
        "FUCK THIS SHIT",
        'print "I\'m out of here"',
    ]

    parsed = backend.parser.parse_end_loop(example_file)

    assert parsed == ['print "I\'m out of here"']
