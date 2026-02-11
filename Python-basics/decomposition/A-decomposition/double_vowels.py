# Write a function `double_vowel` that accepts a string as an argument.
# The function should return a new string where every vowel
# (a, e, i, o, u) is repeated twice consecutively.

def double_vowel(s):
    vowels = "aeiou"
    result = ""

    for char in s:
        result += char
        if char in vowels:
            result += char

    return result


print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'
