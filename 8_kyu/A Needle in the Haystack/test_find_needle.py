from find_needle import find_needle


def run_test(arr, n, s=''):
    found = 'found the needle at position '
    assert find_needle(arr) == f'{found}{n}'


def test_find_needle():
    haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True,
                                        False]
    run_test(haystack, 3)

    haystack = ['283497238987234', 'a dog', 'a cat', 'some random junk',
                'a piece of hay', 'needle',
                'something somebody lost a while ago']
    run_test(haystack, 5)

    haystack = [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 5, 4, 3, 4, 5, 6, 67, 5, 5, 3, 3,
                4, 2, 34, 234, 23, 4, 234, 324, 324, 'needle', 1, 2, 3, 4, 5,
                5, 6, 5, 4, 32, 3, 45, 54]
    run_test(haystack, 30)
