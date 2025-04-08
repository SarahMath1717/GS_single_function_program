from lib.make_snippet import *

def test_make_snippet_long():
    result = make_snippet("red, orange, yellow, green, blue, indigo, violet")
    assert result == "red, orange, yellow, green, blue..."

def test_make_snippet_short():
    result = make_snippet("blue, purple, pink")
    assert result == "blue, purple, pink"