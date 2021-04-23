"""Adjacent repeated words in a string"""


def count_adjacent_pairs(st):
    adjacents = 0
    prev_word = ""
    new_group = False

    for word in st.split(" "):
        word = word.lower()
        if word != prev_word:
            new_group = True
            prev_word = word
        else:
            if new_group:
                adjacents += 1
                new_group = False
    return adjacents
