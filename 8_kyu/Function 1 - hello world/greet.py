'''Function 1 - hello world
'''
import binascii


def greet():
    bin_hex = b'48656c6c6f20576f726c6421'
    return str(binascii.unhexlify(bin_hex), 'ascii')
