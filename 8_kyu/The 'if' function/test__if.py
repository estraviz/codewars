from _if import _if


a = False
b = False
c = False
d = False
e = False


def a1():
    global a
    a = True


def a2():
    global a
    a = False


def b1():
    global b
    b = False


def b2():
    global b
    b = True


def c1():
    global c
    c = True


def c2():
    global c
    c = False


def d1():
    global d
    d = True


def d2():
    global d
    d = False


def e1():
    global e
    e = True


def e2():
    global e
    e = False


def test__if():
    _if(True, a1, a2)
    _if(False, b1, b2)
    _if(1, c1, c2)
    _if((3 < 4), d1, d2)
    _if((9 % 3 == 0), e1, e2)

    assert (a and b and c and d and e) is True
