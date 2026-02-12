# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(str):
    vowels = "aeiou"
    
    # Go backwards through the string
    for i in range(len(str) - 1, -1, -1):
        if str[i] in vowels:
            return str[:i] + str[i+1:]
    
    # If no vowel is found, return the original string
    return str


print(remove_last_vowel("speaker"))  # 'speakr'
print(remove_last_vowel("trading"))  # 'tradng'
print(remove_last_vowel("thunder"))  # 'thundr'
print(remove_last_vowel("myth"))     # 'myth'
