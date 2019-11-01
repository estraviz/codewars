from vaporcode import vaporcode


def test_vaporcode():
    res = "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
    assert vaporcode("Lets go to the movies") == res

    res = "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
    vaporcode("Why isn't my code working?") == res
