# Electronics #1. Ohm's Law
def ohms_law(s):
    V = R = I = 0
    for input in s.split(' '):
        if input.endswith('V'):
            V = float(input[:-1])
        elif input.endswith('R'):
            R = float(input[:-1])
        elif input.endswith('A'):
            I = float(input[:-1])

    if not V:
        return f'{round(R * I, 6)}V'
    elif not R:
        return f'{round(V / I, 6)}R'
    elif not I:
        return f'{round(V / R, 6)}A'
