"""Did she say hallo?"""

import re


def validate_hello(greetings):
    hello_list = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    regex = re.compile('[^a-zA-Z]')
    for word in greetings.split():
        if regex.sub('', word.lower()) in hello_list:
            return True
    return False
