# -*- coding: utf-8 -*-
from solution import dative
import pytest


@pytest.mark.parametrize(
    "word, result",
    [[u"ablak", u"ablaknak"],
     [u"tükör", u"tükörnek"],
     [u"keret", u"keretnek"],
     [u"otthon", u"otthonnak"],
     [u"virág", u"virágnak"],
     [u"tett", u"tettnek"],
     [u"rokkant", u"rokkantnak"],
     [u"rossz", u"rossznak"]])
def test_dative(word, result):
    assert dative(word) == result
