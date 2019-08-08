from sort_by_length import sort_by_length

tests = [
    [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
    [["", "pizza", "brains", "moderately"],
     ["", "moderately", "brains", "pizza"]],
    [["short", "longer", "longest"], ["longer", "longest", "short"]],
    [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
    [["", "bees", "eloquent", "dictionary"],
     ["", "dictionary", "eloquent", "bees"]],
    [["a short sentence", "a longer sentence", "the longest sentence"],
     ["a longer sentence", "the longest sentence", "a short sentence"]],
]


def test_sort_by_length():
    for exp, inp in tests:
        assert sort_by_length(inp) == exp
