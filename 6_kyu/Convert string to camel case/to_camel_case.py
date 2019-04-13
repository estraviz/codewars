"""Convert string to camel case
"""
import re


def to_camel_case(text):
    return "" if len(text) == 0 \
      else "".join([word if i == 0 and word[0] == word[0].lower()
                    else word.capitalize()
                    for i, word in enumerate(re.split(r'-|_', text))])
