from goose_filter import goose_filter


def test_goose_filter():
    a = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse",
         "Blue Swedish"]
    b = ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
    assert goose_filter(a) == b

    a = ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
    b = ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
    assert goose_filter(a) == b

    a = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    b = []
    assert goose_filter(a) == b
