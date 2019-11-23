"""
Russian postal code checker
"""


def zipvalidate(postcode):
    if len(postcode) != 6:
        return False
    try:
        int(postcode)
        return False if postcode[0] in {'0', '5', '7', '8', '9'} else True
    except:
        return False
