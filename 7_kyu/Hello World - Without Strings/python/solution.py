# Hello World - Without Strings
def hello_world():
    return str().join(
        chr(c) for c in [
            72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33
        ]
    )
