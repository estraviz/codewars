# last digits of a number
def solution(n, d):
    output = []
    if d > 0:
        lst = list(int(d) for d in str(n))
        output = lst if d > len(lst) else lst[len(lst)-d:]
    return output
