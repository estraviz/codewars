"""Binary to Text (ASCII) Conversion"""


def binary_to_string(binary):
    return "".join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
