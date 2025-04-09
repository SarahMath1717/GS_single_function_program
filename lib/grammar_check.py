# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

def check_grammar(string):
    if string[-1] in (".", "!", "?") and string[0].isupper():
        return True
    else:
        return False


