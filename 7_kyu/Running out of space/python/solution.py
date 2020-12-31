"""Running out of space"""


def spacey(array):
    aux = ""
    output = []
    for word in array:
        aux += word
        output.append(aux)
    return output
