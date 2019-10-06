from histogram import histogram


def test_histogram():
    res = """6|##### 5
    5|
    4|# 1
    3|########## 10
    2|### 3
    1|####### 7
    """
    res = '6|##### 5\n5|\n4|# 1\n3|########## 10\n2|### 3\n1|####### 7\n'
    assert histogram([7, 3, 10, 1, 0, 5]) == res

    res = """6|
    5|
    4|
    3|
    2|
    1|
    """
    res = '6|\n5|\n4|\n3|\n2|\n1|\n'
    assert histogram([0, 0, 0, 0, 0, 0]) == res
