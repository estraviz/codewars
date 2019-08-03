"""
Decode the Morse code
"""

from morse_table import MORSE_CODE


def decode_morse(morse_code):
    return ''.join(
        MORSE_CODE.get(char, ' ')
        for char in morse_code.lstrip().split(' ')).replace('  ',
                                                            ' ').rstrip()
