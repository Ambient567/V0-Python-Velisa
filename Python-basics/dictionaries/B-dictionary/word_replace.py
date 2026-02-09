# Write a function `word_replace` that accepts:
# - a sentence string
# - a dictionary
# The function should return a new sentence where words that appear as keys
# in the dictionary are replaced with their corresponding values.

def word_replace(sentence, mapping):
    words = sentence.split()          # Split sentence into words
    new_words = []
    for word in words:
        if word in mapping:           # Replace word if it exists in mapping
            new_words.append(mapping[word])
        else:
            new_words.append(word)
    return " ".join(new_words)       # Join words back into a sentence


print(word_replace(
    "I never take naps during the day",
    {"never":"always","day":"weekend"}
))
# 'I always take naps during the weekend'

print(word_replace(
    "the park is closed",
    {"closed":"open","the":"a"}
))
# 'a park is open'

print(word_replace(
    "I do what I want",
    {"I":"we","cat":"dog"}
))

