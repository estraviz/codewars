"""The Vowel Code"""

vowels = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
numbers = {v: k for k, v in vowels.items()}


def encode(st):
    return ''.join(vowels.get(c, c) for c in st)


def decode(st):
    return ''.join(numbers.get(c, c) for c in st)
