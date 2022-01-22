# Counting Duplicates Across Multiple Lists
def count_duplicates(name, age, height):
    tuples = []
    duplicates = 0
    for n, a, h in zip(name, age, height):
        if [n, a, h] in tuples:
            duplicates += 1
        else:
            tuples.append([n, a, h])
    return duplicates
