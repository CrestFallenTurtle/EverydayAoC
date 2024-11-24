import pytest

import backend.tools


def test_split_up_args() -> None:
    example_args = ["1,2,3,4,5", "$a,$b,69, 420"]

    result = backend.tools.split_up_args(example_args)

    assert result == ["1", "2", "3", "4", "5", "$a", "$b", "69", "420"]


@pytest.mark.skip("Annoying to test")
def test_collect_python_files() -> None:
    pass
