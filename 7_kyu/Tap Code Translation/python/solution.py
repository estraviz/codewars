"""Tap Code Translation"""


def tap_code_translation(text):
    polybius = ["ABCDE", "FGHIJ", "LMNOP", "QRSTU", "VWXYZ"]
    output = []
    for c in text.replace('k', 'c').upper():
        for i, chunk in enumerate(polybius):
            if c in chunk:
                output.append('.' * (i + 1) + ' ' + '.' * (chunk.index(c) + 1))
                break
    return " ".join(output)
