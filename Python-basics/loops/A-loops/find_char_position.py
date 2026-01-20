# Write a function that prints all **indexes** where a character appears in a string.

def find_char_positions(str, ch):
    for x in range(len(str)):
        if ch == str[x]:
            print(x)
        

find_char_positions("banana", "a")
# 1
# 3
# 5
