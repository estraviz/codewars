"""Hungarian Vowel Harmony (easy)
"""
# -*- coding: utf-8 -*-
FRONT_VOWELS = {'e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'}
BACK_VOWELS = {'a', 'á', 'o', 'ó', 'u', 'ú'}


def dative(word):
    for chr in word[::-1]:
        if chr in FRONT_VOWELS:
            word += "nek"
            break
        elif chr in BACK_VOWELS:
            word += "nak"
            break
        else:
            continue
    return word
