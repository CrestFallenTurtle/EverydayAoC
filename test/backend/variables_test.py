import backend.variables


def test_get_variable_name() -> None:
    expected = {"var": "var", "$var": "var"}

    for key, value in expected.items():

        assert backend.variables.get_variable_name(key) == value


def test_try_get_variable_value() -> None:

    namespace = {"var": 69}

    result = backend.variables.try_get_variable_value("$var", namespace)

    assert result == 69
