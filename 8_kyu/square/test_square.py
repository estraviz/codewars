from square import square


test = [1, 2, 3, 5, 7, 11]
result = [1, 4, 9, 25, 49, 121]


def test_square():
    for i, each in enumerate(test):
        assert square(each) == result[i]
