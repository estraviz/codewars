from name_shuffler import name_shuffler


def test_name_shuffler():
    assert name_shuffler('john McClane') == 'McClane john'
    assert name_shuffler('Mary jeggins') == 'jeggins Mary'
    assert name_shuffler('tom jerry') == 'jerry tom'
    assert name_shuffler('Mary Jane') == 'Jane Mary'
    assert name_shuffler('John Doe') == 'Doe John'
    assert name_shuffler('William O\'Brien') == 'O\'Brien William'
    assert name_shuffler('George Huffingquane-McGafferty') == \
        'Huffingquane-McGafferty George'
