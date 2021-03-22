"""Fizz Buzz"""

mults = {
    3: 'Fizz',
    5: 'Buzz',
}


def fizzbuzz(n):
    output = []
    for i in range(1, n+1):
        temp = ""
        for j in mults.keys():
            if i % j == 0:
                temp += mults.get(j)
        output.append(temp if temp else i)
    return output
