"""
Polish alphabet
"""


def correct_polish_letters(st):
    diacritics = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z'
    }
    return ''.join([diacritics.get(chr, chr) for chr in st])
