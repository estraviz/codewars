# Positions Average
def pos_average(s):
    strings = s.split(", ")
    len_s = len(strings)
    commons = 0
    comparisons = 0
    for i in range(0, len_s-1):
        for j in range(i+1, len_s):
            x, y = strings[i], strings[j]
            commons += sum(a == b for a, b in zip(x, y))
            comparisons += 1
    num_digits = len(strings[0])
    return round(commons / (comparisons * num_digits) * 100, 10)
