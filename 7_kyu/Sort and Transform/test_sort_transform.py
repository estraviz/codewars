from sort_transform import sort_transform


def test_sort_transform():
    arr = [111, 112, 113, 114, 115, 113, 114, 110]
    assert sort_transform(arr) == "oprn-nors-sron-nors"

    arr = [51, 62, 73, 84, 95, 100, 99, 126]
    assert sort_transform(arr) == "3>c~-3>d~-~d>3-3>d~"

    arr = [66, 101, 55, 111, 113]
    assert sort_transform(arr) == "Beoq-7Boq-qoB7-7Boq"

    arr = [78, 117, 110, 99, 104, 117, 107, 115, 120, 121, 125]
    assert sort_transform(arr) == "Nuy}-Ncy}-}ycN-Ncy}"

    arr = [101, 48, 75, 105, 99, 107, 121, 122, 124]
    assert sort_transform(arr) == "e0z|-0Kz|-|zK0-0Kz|"

    arr = [80, 117, 115, 104, 65, 85, 112, 115, 66, 76, 62]
    assert sort_transform(arr) == "PuL>->Asu-usA>->Asu"

    arr = [91, 100, 111, 121, 51, 62, 81, 92, 63]
    assert sort_transform(arr) == "[d\\?-3>oy-yo>3-3>oy"

    arr = [78, 93, 92, 98, 108, 119, 116, 100, 85, 80]
    assert sort_transform(arr) == "N]UP-NPtw-wtPN-NPtw"

    arr = [111, 121, 122, 124, 125, 126, 117, 118, 119, 121, 122, 73]
    assert sort_transform(arr) == "oyzI-Io}~-~}oI-Io}~"

    arr = [82, 98, 72, 71, 71, 72, 62, 67, 68, 115, 117, 112, 122, 121, 93]
    assert sort_transform(arr) == "Rby]->Cyz-zyC>->Cyz"

    arr = [99, 98, 97, 96, 81, 82, 82]
    assert sort_transform(arr) == "cbRR-QRbc-cbRQ-QRbc"

    arr = [66, 99, 88, 122, 123, 110]
    assert sort_transform(arr) == "Bc{n-BXz{-{zXB-BXz{"

    arr = [66, 87, 98, 59, 57, 50, 51, 52]
    assert sort_transform(arr) == "BW34-23Wb-bW32-23Wb"
