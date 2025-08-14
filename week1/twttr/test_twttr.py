import sys
import os
from twttr import shorten



def test_shorten_wInput():
    assert shorten("emre") == "mr"
    assert shorten("david") == "dvd"
    assert shorten("twitter") == "twttr"
    assert shorten("AExUIO") == "x"
    assert shorten(",.!@#") == ",.!@#"



def test_shorten_woInput():
    assert shorten("") == ""



def test_shorten_number():
    assert shorten("1234") == "1234"