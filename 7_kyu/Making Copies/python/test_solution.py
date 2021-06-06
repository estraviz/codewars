import pytest

from solution import copy_list


@pytest.mark.parametrize(
    "t, t_copy",
    [
        ([1, 2, 3, 4], [1, 2, 3, 4]),
    ]
)
def test_copy_list(t, t_copy):
    assert copy_list(t) == t_copy


@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize(
    "t, t_copy",
    [
        ([1, 2, 3, 4], [1, 2, 3, 4]),
    ]
)
def test_copy_should_not_be_the_same_anymore(t, t_copy):
    t[1] += 5
    assert copy_list(t) == t_copy
