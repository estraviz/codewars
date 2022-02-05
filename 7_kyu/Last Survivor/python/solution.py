# Last Survivor
def last_survivor(letters, coords):
    letters = list(letters)
    while len(letters) > 1:
        for coord in coords:
            letters.pop(coord)
    return "".join(letters)
