from friend import friend


def test_friend():
    assert friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"]
    assert friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]) == ["Ryan"]

    names = ["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]
    assert friend(names) == ["Jimm", "Cari", "aret"]

    assert friend(["Love", "Your", "Face", "1"]) == ["Love", "Your", "Face"]

    names = ["Hell", "Is", "a", "badd", "word"]
    assert friend(names) == ["Hell", "badd", "word"]

    assert friend(["Issa", "Issac", "Issacs", "ISISS"]) == ["Issa"]
    assert friend(["Robot", "Your", "MOMOMOMO"]) == ["Your"]
    assert friend(["Your", "BUTT"]) == ["Your", "BUTT"]
    assert friend(["Hello", "I", "AM", "Sanjay", "Gupt"]) == ["Gupt"]

    names = ["This", "IS", "enough", "TEst", "CaSe"]
    assert friend(names) == ["This", "TEst", "CaSe"]

    assert friend([]) == []
