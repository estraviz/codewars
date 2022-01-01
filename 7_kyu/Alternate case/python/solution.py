# Alternate case
def alternate_case(s):
    return "".join(
        chr(
            ord(c) + 32 * (1 if c.isupper() else -1 if c.islower() else 0)
        ) for c in s
    )
