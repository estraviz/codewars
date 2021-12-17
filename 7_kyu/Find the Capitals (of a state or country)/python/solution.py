# Find the Capitals
def capital(capitals):
    output = []
    for capital in capitals:
        for k, v in capital.items():
            if k == 'capital':
                c = v
            else:
                s = v
        output.append(f"The capital of {s} is {c}")
    return output
