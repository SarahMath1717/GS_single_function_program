from lib.make_snippet import *

def test_make_snipet_length():
    result = make_snippet("red, orange, yellow, green, blue, indigo, violet")
    assert result == f"red, orange, yellow, green, blue..."