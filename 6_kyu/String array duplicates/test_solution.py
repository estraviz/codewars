from solution import dup


def test_solution():
    arr = ["ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"]
    assert dup(arr) == ['codewars', 'picaniny', 'hubububo']

    arr = ["abracadabra", "allottee", "assessee"]
    assert dup(arr) == ['abracadabra', 'alote', 'asese']

    arr = ["kelless", "keenness"]
    assert dup(arr) == ['keles', 'kenes']

    arr = ["Woolloomooloo", "flooddoorroommoonlighters", "chuchchi"]
    assert dup(arr), ['Wolomolo', 'flodoromonlighters', 'chuchchi']

    arr = ["adanac", "soonness", "toolless", "ppellee"]
    assert dup(arr) == ['adanac', 'sones', 'toles', 'pele']

    arr = ["callalloo", "feelless", "heelless"]
    assert dup(arr) == ['calalo', 'feles', 'heles']

    arr = ["putteellinen", "keenness"]
    assert dup(arr) == ['putelinen', 'kenes']

    arr = ["kelless", "voorraaddoosspullen", "achcha"]
    assert dup(arr) == ['keles', 'voradospulen', 'achcha']
