from decode_morse import decode_morse


def test_example_from_description():
    assert decode_morse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE'


def test_basic_morse_decoding():
    assert decode_morse('.-') == 'A'
    assert decode_morse('.') == 'E'
    assert decode_morse('..') == 'I'
    assert decode_morse('. .') == 'EE'
    assert decode_morse('.   .') == 'E E'
    assert decode_morse('...---...') == 'SOS'
    assert decode_morse('... --- ...') == 'SOS'
    assert decode_morse('...   ---   ...') == 'S O S'


def test_extra_zeros_handling():
    assert decode_morse(' . ') == 'E'
    assert decode_morse('   .   . ') == 'E E'


def test_complex_tests():
    a = '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   ' + \
        '-... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   ' + \
        '--- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '
    b = 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
    assert decode_morse(a) == b
