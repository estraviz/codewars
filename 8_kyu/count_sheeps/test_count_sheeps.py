from count_sheeps import count_sheeps


array1 = [True, True, True, False, True, True,
          True, True, True, False, True, False,
          True, False, False, True, True, True,
          True, True, False, False, True,  True]

array2 = []
array2.extend([True] * 500)
array2.extend([None] * 5)
array2.extend([False] * 100)

array3 = []


def test_count_sheeps():
    assert count_sheeps(array1) == 17
    assert count_sheeps(array2) == 500
    assert count_sheeps(array3) == 0
