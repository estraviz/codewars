from in_array import in_array


def test_one():
    a1 = ["live", "arp", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp', 'live', 'strong']
    assert in_array(a1, a2) == r


def test_two():
    a1 = ["arp", "mice", "bull"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp']
    assert in_array(a1, a2) == r


def test_three():
    a1 = ["cod", "code", "wars", "ewar"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong", "codewars"]
    r = ["cod", "code", "ewar", "wars"]
    assert in_array(a1, a2) == r


def test_four():
    a1 = ["cod", "code", "wars", "ewar", "ar"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong", "codewars"]
    r = ["ar", "cod", "code", "ewar", "wars"]
    assert in_array(a1, a2) == r


def test_five():
    a1 = ["cod", "code", "wars", "ewar", "ar"]
    a2 = []
    r = []
    assert in_array(a1, a2) == r


def test_six():
    a1 = ["1295", "code", "1346", "1028", "ar"]
    a2 = ["12951295", "ode", "46", "10281066", "par"]
    r = ["1028", "1295", "ar"]
    assert in_array(a1, a2) == r


def test_seven():
    a1 = ["&()", "code", "1346", "1028", "ar"]
    a2 = ["12&()95", "coderange", "46", "1066", "par"]
    r = ["&()", "ar", "code"]
    assert in_array(a1, a2) == r


def test_eight():
    a1 = ["ohio", "code", "1346", "1028", "art"]
    a2 = ["Carolina", "Ohio", "4600", "NY", "California"]
    r = []
    assert in_array(a1, a2) == r


def test_nine():
    a1 = ["duplicates", "duplicates"]
    a2 = ["duplicates", "duplicates"]
    r = ["duplicates"]
    assert in_array(a1, a2) == r
