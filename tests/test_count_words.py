from lib.count_words import *

def test_count_word():
    result = count_words("Damnit")
    assert result == 1

def test_count_words_without_special_characters():
    result = count_words("My coffee is gone")
    assert result == 4

def test_count_words_with_special_characters():
    result = count_words("where did I leave my cup of coffee, and is it cold?")
    assert result == 12