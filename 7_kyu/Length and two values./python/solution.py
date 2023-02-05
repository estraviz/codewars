def alternate(n, first_value, second_value):
    return [first_value if i % 2 == 0 else second_value for i in range(n)]
