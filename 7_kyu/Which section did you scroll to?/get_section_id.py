"""
Which section did you scroll to?
"""


def get_section_id(scroll, sizes):
    total = 0
    for i, size in enumerate(sizes):
        total += size
        if scroll >= total:
            continue
        else:
            return i
    else:
        return -1
