"""Where is my parent!?(cry)"""

def find_children(dancing_brigade):
    return "".join(sorted(sorted(dancing_brigade), key=str.lower))
