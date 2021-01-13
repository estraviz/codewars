import pytest

from solution import dir_reduc


@pytest.mark.parametrize(
    "arr, result",
    [
        (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], ["WEST"]),
        (["NORTH", "WEST", "SOUTH", "EAST"], ["NORTH", "WEST", "SOUTH", "EAST"]),
        (
            [
                "NORTH",
                "SOUTH",
                "EAST",
                "WEST",
                "NORTH",
                "NORTH",
                "SOUTH",
                "NORTH",
                "WEST",
                "EAST",
            ],
            ["NORTH", "NORTH"],
        ),
        ([], []),
        (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"], []),
        (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"], ["NORTH"]),
        (
            [
                "EAST",
                "EAST",
                "WEST",
                "NORTH",
                "WEST",
                "EAST",
                "EAST",
                "SOUTH",
                "NORTH",
                "WEST",
            ],
            ["EAST", "NORTH"],
        ),
        (
            [
                "NORTH",
                "EAST",
                "NORTH",
                "EAST",
                "WEST",
                "WEST",
                "EAST",
                "EAST",
                "WEST",
                "SOUTH",
            ],
            ["NORTH", "EAST"],
        ),
        (
            [
                "NORTH",
                "NORTH",
                "EAST",
                "SOUTH",
                "EAST",
                "EAST",
                "SOUTH",
                "SOUTH",
                "SOUTH",
                "NORTH",
            ],
            ["NORTH", "NORTH", "EAST", "SOUTH", "EAST", "EAST", "SOUTH", "SOUTH"],
        ),
    ],
)
def test_dir_reduc(arr, result):
    assert dir_reduc(arr) == result
