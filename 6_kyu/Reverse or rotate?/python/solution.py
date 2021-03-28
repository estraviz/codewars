"""Reverse or rotate?"""


def revrot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ""

    chunks = []
    i = 0
    while i < len(strng):
        chunk = strng[i:i+sz]
        if len(chunk) >= sz:
            chunk = chunk[::-1] if sum(int(i)**3 for i in chunk) % 2 == 0 \
                                else chunk[1:] + chunk[0]
            chunks.append(chunk)
        i += sz
    return "".join(chunks)
