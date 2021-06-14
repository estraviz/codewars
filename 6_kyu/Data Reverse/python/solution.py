"""Data Reverse"""

CHUNK_SIZE = 8


def data_reverse(data):
    output = []
    i = 0
    while i*CHUNK_SIZE <= len(data):
        output += data[len(data)-(i+1)*CHUNK_SIZE:len(data)-i*CHUNK_SIZE:]
        i += 1
    return output
