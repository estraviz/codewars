"""
Filter out the geese
"""

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [elem for elem in birds if elem not in geese]
