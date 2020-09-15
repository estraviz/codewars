"""String array duplicates
"""


def dup(arr):
    prev_chr = ''
    clean_word = ""
    output = []
    for word in arr:
        for chr in word:
            if chr != prev_chr:
                clean_word += chr
            prev_chr = chr
        output.append(clean_word)
        clean_word = ""
        prev_chr = ''
    return output
