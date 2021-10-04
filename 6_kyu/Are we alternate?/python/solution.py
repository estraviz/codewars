"""Are we alternate?"""


def is_alt(s):
    first_vowel = next((i for i, c in enumerate(s) if c in 'aeiou'), -1)
    if first_vowel > 1:
        return False
    for c in s[first_vowel::2]:
        if c not in set('aeiou'):
            return False
    for c in s[first_vowel+1::2]:
        if c in set('aeiou'):
            return False
    return True
