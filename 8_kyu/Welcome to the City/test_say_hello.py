from say_hello import say_hello


def test_basic_tests():
    out = 'Hello, John Smith! Welcome to Phoenix, Arizona!'
    assert say_hello(['John', 'Smith'], 'Phoenix', 'Arizona') == out

    out = 'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!'
    assert say_hello(['Franklin', 'Delano', 'Roosevelt'], 'Chicago',
                     'Illinois') == out

    out = 'Hello, Wallace Russel Osbourne! Welcome to Albany, New York!'
    assert say_hello(['Wallace', 'Russel', 'Osbourne'], 'Albany', 'New York') \
        == out

    out = 'Hello, Lupin the Third! Welcome to Los Angeles, California!'
    assert say_hello(['Lupin', 'the', 'Third'], 'Los Angeles', 'California') \
        == out

    out = 'Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!'
    assert say_hello(['Marlo', 'Stanfield'], 'Baltimore', 'Maryland') == out
