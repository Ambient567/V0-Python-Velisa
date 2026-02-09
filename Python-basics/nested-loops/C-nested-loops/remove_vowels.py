# Write a function remove_vowels(s) that accepts a string and returns a new string # with all vowels removed (a, e, i, o, u).

def remove_vowels(s):
    vowels = "aeiou"
    result = ""
    for char in s:
        if char.lower() not in vowels:
            result += char
    return result


# Example usage:
print(remove_vowels("jello"))           # 'jll'
print(remove_vowels("sensitivity"))     # 'snstvty'
print(remove_vowels("cellar door"))     # 'cllr dr'

