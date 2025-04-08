# A function called count_words that takes a string as an argument 
# and returns the number of words in that string.

def count_words(string):
    words_in_string = string.split(" ")
    return len(words_in_string)