# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

def make_acronym(sentence):
    words = sentence.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
        
    print(acronym)


# Example:
make_acronym("New York") #-> 'NY'
make_acronym("same stuff different day") # -> 'SSDD'
make_acronym("Laugh out loud")# -> 'LOL'
make_acronym("don't over think stuff")# -> 'DOTS'

