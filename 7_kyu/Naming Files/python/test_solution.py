import pytest

from solution import name_file


data = [
    ('IMG <index_no>', 4, 1, ["IMG 1", "IMG 2", "IMG 3", "IMG 4"]),
    ('image #<index_no>.jpg', 3, 7, ["image #7.jpg", "image #8.jpg", "image #9.jpg"]),
    ('#<index_no> #<index_no>', 3, -2, ["#-2 #-2", "#-1 #-1", "#0 #0"]),
    ('<file> number <index_no>', 5, 0, ["<file> number 0", "<file> number 1", "<file> number 2", "<file> number 3", "<file> number 4"]),
    ('<file_no> number <index_no>', 2, -1, ["<file_no> number -1", "<file_no> number 0"]),
    ('file', 2, 3, ["file", "file"]),
    ('<file_no> number <index_no>', -1, 0, []),
    ('file <index_no>', 2, 0.1, []),
    ('file <index_no>', 0.2, 0, []),
    ('file <index_no>', 0, 0, []),
]


@pytest.mark.parametrize(
    "fmt, nbr, start, result", data
)
def test_name_file(fmt, nbr, start, result):
    assert name_file(fmt, nbr, start) == result
