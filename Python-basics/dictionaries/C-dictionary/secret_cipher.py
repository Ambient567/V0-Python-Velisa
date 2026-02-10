# Write a function `secret_cipher` that accepts:
# - a string
# - a dictionary (cipher map)
# Rules:
# - Replace each character in the string with its corresponding value from the dictionary
# - If a character does not exist as a key in the dictionary, replace it with "?"
# - Return the resulting string

def secret_cipher(s, cipher):
    result = ""
    for char in s:
        if char in cipher:
            result += cipher[char]
        else:
            result += "?"
    return result


print(secret_cipher("jello", {"j":"r","l":"s","e":"i"}))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j"}))
# 'p?m?o?j'
