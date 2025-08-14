from um import count
import pytest




def test_um():
    assert count("hello, um, world") == 1
    assert count("hello, UM, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("123") == 0
    assert count("12um12") == 0
    assert count("") == 0


