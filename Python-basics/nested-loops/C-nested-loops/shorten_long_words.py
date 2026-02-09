# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.

def shorten_long_words(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if len(word) > 4:
            new_word = ""
            for char in word:
                if char.lower() not in vowels:
                    new_word += char
            result.append(new_word)
        else:
            result.append(word)

    return " ".join(result)


# Example usage:
print(shorten_long_words("they are very noble people"))  
# 'they are very nbl ppl'

print(shorten_long_words("stick with it"))  
# 'stck with it'

print(shorten_long_words("ballerina, you must have seen her"))  
# 'bllrna, you must have seen her'
