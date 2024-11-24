import pytest

import backend.namespace


@pytest.mark.skip("Annoying to test")
def test_create_lib_namespace() -> None:
    pass


def test_create_var_namespace() -> None:
    example_parsed = ["A = 20", "B = 30", "C = 40"]

    result = backend.namespace.create_var_namespace(example_parsed)

    assert result == {"A": 20, "B": 30, "C": 40}


def test_test_parse_method_section() -> None:
    example_parsed = ["foo:", "print $str", "add $a, $b, $c"]

    result = backend.namespace.create_method_namespace(example_parsed)

    assert result == {"foo": ["print $str", "add $a, $b, $c"]}
