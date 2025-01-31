"""FIXME: Replace all dots
"""
import re


def replace_dots(str):
    return re.sub(r"[.]", "-", str)
