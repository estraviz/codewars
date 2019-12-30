"""
Crash Override
"""

FIRST_NAME = {
    'A': 'Alpha',
    'B': 'Beta',
    'C': 'Cache',
    'D': 'Data',
    'E': 'Energy',
    'F': 'Function',
    'G': 'Glitch',
    'H': 'Half-life',
    'I': 'Ice',
    'J': 'Java',
    'K': 'Keystroke',
    'L': 'Logic',
    'M': 'Malware',
    'N': 'Nagware',
    'O': 'OS',
    'P': 'Phishing',
    'Q': 'Quantum',
    'R': 'RAD',
    'S': 'Strike',
    'T': 'Trojan',
    'U': 'Ultraviolet',
    'V': 'Vanilla',
    'W': 'WiFi',
    'X': 'Xerox',
    'Y': 'Y',
    'Z': 'Zero'
}
SURNAME = {
    'A': 'Analogue',
    'B': 'Bomb',
    'C': 'Catalyst',
    'D': 'Discharge',
    'E': 'Electron',
    'F': 'Faraday',
    'G': 'Gig',
    'H': 'Hacker',
    'I': 'IP',
    'J': 'Jabber',
    'K': 'Killer',
    'L': 'Lazer',
    'M': 'Mike',
    'N': 'n00b',
    'O': 'Overclock',
    'P': 'Payload',
    'Q': 'Quark',
    'R': 'Roy',
    'S': 'Spy',
    'T': 'T-Rex',
    'U': 'Unit',
    'V': 'Virus',
    'W': 'Worm',
    'X': 'X',
    'Y': 'Yob',
    'Z': 'Zombie'
}


def alias_gen(f_name, l_name):
    first = FIRST_NAME.get(f_name.title()[0])
    second = SURNAME.get(l_name.title()[0])
    return f'{first} {second}' \
        if first and second \
        else "Your name must start with a letter from A - Z."
