from positive_sum import positive_sum


def test_positive_sum():
    assert positive_sum([1, 2, 3, 4, 5]) == 15
    assert positive_sum([1, -2, 3, 4, 5]) == 13
    assert positive_sum([-1, 2, 3, 4, -5]) == 9
    assert positive_sum([]) == 0
    assert positive_sum([-1, -2, -3, -4, -5]) == 0
