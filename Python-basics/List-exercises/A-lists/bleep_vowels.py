# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.

def bleep_vowels(text):
    vowels = "aeiou"
    new_str = ""

    for str in range(len(text)):
        if text[str] in vowels:
            new_str += "*"
        else:
            new_str += text[str]

    print(new_str)

# Example:
bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'

