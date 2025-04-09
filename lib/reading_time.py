# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, 
# assuming that I can read 200 words a minute.

def read_time (string):
    count_words = string.split(" ")
    total_words = len(count_words)
    return (total_words) / 200