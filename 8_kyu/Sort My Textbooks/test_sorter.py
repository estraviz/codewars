from sorter import sorter


def test_sorter():
    arr_in = ['Algebra', 'History', 'Geometry', 'English']
    arr_out = ['Algebra', 'English', 'Geometry', 'History']
    assert sorter(arr_in) == arr_out

    arr_in = ['Algebra', 'history', 'Geometry', 'english']
    arr_out = ['Algebra', 'english', 'Geometry', 'history']
    assert sorter(arr_in) == arr_out

    arr_in = ['Alg#bra', '$istory', 'Geom^try', '**english']
    arr_out = ['$istory', '**english', 'Alg#bra', 'Geom^try']
    assert sorter(arr_in) == arr_out
