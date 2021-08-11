"""Split In Parts"""


def split_in_parts(s, part_len):
    return " ".join(s[i: i + part_len] for i in range(0, len(s), part_len))
