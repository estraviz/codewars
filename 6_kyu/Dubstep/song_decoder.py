"""Dubstep
"""
import re


def song_decoder(song):
    return re.sub(r'(WUB)+', r' ', song).strip()
