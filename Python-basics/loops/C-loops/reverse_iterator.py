# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.

def reverse_iterate(text):
    for x in range(len(text),0,-1):
        print(text[x-1])

# Example:
reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

reverse_iterate("box")
# x
# o
# b

