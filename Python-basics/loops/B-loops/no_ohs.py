# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

def no_ohs(word):
    for ch in word:
        if ch != "o":
            print(ch)


# Example:
no_ohs("code")
# c
# d
# e

