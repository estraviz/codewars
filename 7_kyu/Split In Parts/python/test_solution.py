import pytest

from solution import split_in_parts


tests = [
    ("supercalifragilisticexpialidocious", 3,
     "sup erc ali fra gil ist ice xpi ali doc iou s"),
    ("HelloKata", 1, "H e l l o K a t a"),
    ("HelloKata", 9, "HelloKata"),
]


@pytest.mark.parametrize(
    "s, part_length, expected", tests
)
def test_split_in_parts(s, part_length, expected):
    assert split_in_parts(s, part_length) == expected
