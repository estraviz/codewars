"""Sum of Triangular Numbers"""


def sum_triangular_numbers(n):
    matrix = build_triangle(n)
    return sum(matrix[i][-1] for i in range(n))


def build_triangle(n, start=0):
    matrix = []
    for i in range(n):
        matrix.append(row := [j+1 for j in range(start, start+1+i)])
        start = row[-1]
    return matrix
