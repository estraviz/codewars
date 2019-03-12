"""Disemvowel Trolls
"""
import re


def disemvowel(string):
    return re.sub("[aeiouAEIOU]+", "", string)
