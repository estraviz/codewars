from longest_consec import longest_consec


def test_longest_consec():
    arr = ["zone", "abigail", "theta", "form", "libe", "zas"]
    assert longest_consec(arr, 2) == "abigailtheta"

    arr = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb",
           "oocccffuucccjjjkkkjyyyeehh"]
    assert longest_consec(arr, 1) == "oocccffuucccjjjkkkjyyyeehh"

    assert longest_consec([], 3) == ""

    arr = ["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv",
           "vweqilsfytihvrzlaodfixoyxvyuyvgpck"]
    assert longest_consec(arr, 2) == \
        "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"

    arr = ["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"]
    assert longest_consec(arr, 2) == "wlwsasphmxxowiaxujylentrklctozmymu"

    arr = ["zone", "abigail", "theta", "form", "libe", "zas"]
    assert longest_consec(arr, -2) == ""

    arr = ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"]
    assert longest_consec(arr, 3) == "ixoyx3452zzzzzzzzzzzz"

    arr = ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"]
    assert longest_consec(arr, 15) == ""

    arr = ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"]
    assert longest_consec(arr, 0) == ""
