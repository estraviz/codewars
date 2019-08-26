from perimeter import perimeter


def test_perimeter():
    assert perimeter(5) == 80
    assert perimeter(7) == 216
    assert perimeter(20) == 114624
    assert perimeter(30) == 14098308
    assert perimeter(100) == 6002082144827584333104
    assert perimeter(
        500
    ) == 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504
