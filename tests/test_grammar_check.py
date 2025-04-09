from lib.grammar_check import *

# check first letter is capital
def test_check_capital_pass():
    result = check_grammar("This is a sentence.")
    assert result == True

def test_check_capital_fail():
    result = check_grammar("this is a sentence")
    assert result == False

# check sentence ends with appropriate sentence ending SC
def test_check_grammar_last_char_full_stop():
    result = check_grammar("This is a sentence.")
    assert result == True

def test_check_grammar_last_char_exclamation():
    result = check_grammar("This is a sentence!")
    assert result == True

def test_check_grammar_last_char_question_mark():
    result = check_grammar("This is a sentence?")
    assert result == True

def test_check_grammar_last_char_comma():
    result = check_grammar("This is a sentence,")
    assert result == False

def test_check_grammar_last_char_none():
    result = check_grammar("This is a sentence")
    assert result == False