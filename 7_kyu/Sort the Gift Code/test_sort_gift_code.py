from sort_gift_code import sort_gift_code


def test_sort_gift_code():
    res = 'abcdef'
    assert sort_gift_code('abcdef') == res

    res = 'kpqsuvy'
    assert sort_gift_code('pqksuvy') == res

    res = 'abcdefghijklmnopqrstuvwxyz'
    assert sort_gift_code('zyxwvutsrqponmlkjihgfedcba') == res
