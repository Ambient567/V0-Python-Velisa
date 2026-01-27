# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

def alternating_caps(sentence):
    words = sentence.split()
    result = []

    for i in range(len(words)):
        if i % 2 == 0:
            result.append(words[i].lower())
        else:
            result.append(words[i].upper())

    print(" ".join(result))


# Example:
alternating_caps("take them to school")
# 'take THEM to SCHOOL'

alternating_caps("What did ThEy EAT before?")
# 'what DID they EAT before?'

