# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

def string_repeater(text, n):
    str = ""
    for x in range(n):
        str += text

    print(str)

# Example:
string_repeater("q", 4)  #-> 'qqqq'
string_repeater("go", 2) #-> 'gogo'
string_repeater("tac", 3) #-> 'tactactac'

