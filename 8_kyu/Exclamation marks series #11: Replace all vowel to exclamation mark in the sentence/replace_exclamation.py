'''Exclamation marks series #11:
Replace all vowel to exclamation mark in the sentence
'''

import re


def replace_exclamation(s):
    return re.sub(r'["a|A|e|E|i|I|o|O|u|U]', "!", s)
