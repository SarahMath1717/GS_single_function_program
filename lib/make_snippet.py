# A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.

# Count words in string
# Return entire string if <5
#   Identify first 5 items of string if >5
#   Return string + ... for strings >5

def make_snippet(string):
    words = string.split(", ")
    if len(words) > 5:
        snipped_string = ', '.join(words[:5])
        return (f"{snipped_string}...")
    else:
        return string