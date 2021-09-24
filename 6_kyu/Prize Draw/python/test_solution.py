import pytest

from solution import rank


tests = [
    ("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4, "Benjamin"),
    ("Lagon,Lily", [1, 5], 2, "Lagon"),
    ("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8, "Not enough participants"),
    ("", [4, 2, 1, 4, 3, 1, 2], 6, "No participants"),
    ("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2, "Matthew"),
    ("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4, "Abigail"),
    ("Elijah,Michael,Avery,Sophia,Samantha", [2, 1, 5, 2, 2], 3, "Sophia"),
    ("William,Willaim,Olivia,Olivai,Lily,Lyli", [1, 1, 1, 1, 1, 1], 1, "Willaim"),
    ("Addison,William,Jayden", [3, 5, 6], 1, "William"),
    ("Joshua,Grace,Isabella", [1, 5, 4], 1, "Isabella"),
    ("Elijah,Addison", [3, 6], 2, "Elijah"),
    ("Willaim,Liam,Daniel,Alexander", [6, 4, 6, 2], 2, "Daniel"),
    ("Avery,Olivai,Sophia,Michael,Elizabeth,Willaim,Liam", [5, 5, 3, 2, 1, 3, 6], 5, "Sophia"),
    ("Liam,Madison,Lyli,Jacob,Matthew,Michael", [2, 6, 5, 5, 3, 4], 6, "Liam"),
    ("Sophia,Robert,Abigail,Grace,Lagon", [1, 2, 2, 6, 4], 5, "Sophia"),
    ("Samantha,Ella", [5, 6], 1, "Samantha"),
    ("Aubrey,Jayden", [3, 4], 2, "Aubrey"),
    ("Jacob,Elijah", [4, 3], 1, "Elijah"),
]


@pytest.mark.parametrize(
    "st, we, n, expected", tests
)
def test_rank(st, we, n, expected):
    assert rank(st, we, n) == expected
