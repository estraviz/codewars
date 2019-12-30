from alias_gen import alias_gen


def test_alias_gen():
    basic_tests = ((('Mike', 'Millington'),
                    'Malware Mike'), (('Fahima', 'Tash'), 'Function T-Rex'),
                   (('Daisy', 'Petrovic'), 'Data Payload'),
                   (('Barny', 'White'), 'Beta Worm'), (('Hank', 'Kutz'),
                                                       'Half-life Killer'),
                   (('123abc', 'Pinkman'),
                    'Your name must start with a letter from A - Z.'),
                   (('walter', 'white'), 'WiFi Worm'))

    for names, result in basic_tests:
        assert alias_gen(*names) == result
