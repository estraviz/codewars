import random
from binary_array_to_number import binary_array_to_number


def test_simple():
    assert binary_array_to_number([0, 0, 0, 1]) == 1
    assert binary_array_to_number([0, 0, 1, 0]) == 2
    assert binary_array_to_number([1, 1, 1, 1]) == 15
    assert binary_array_to_number([0, 1, 1, 0]) == 6


def test_random():
    for _ in range(50):
        n = random.randint(0, 1000)
        array = [int(x) for x in bin(n)[2:]]
        assert binary_array_to_number(array) == n
