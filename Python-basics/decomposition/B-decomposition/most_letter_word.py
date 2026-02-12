# Write a function `most_letter_word(sentence, char)` that accepts:
# - a sentence string
# - a single character
#
# The function should return the word in the sentence that contains the
# character the greatest number of times.
#
# If there is a tie, return the word that appears first in the sentence.

def most_letter_word(sentence, char):
    words = sentence.split()
    
    max_count = -1
    best_word = ""
    
    for word in words:
        count = 0
        
        # Count how many times char appears in the word
        for letter in word:
            if letter == char:
                count += 1
        
        # Update if this word has more occurrences
        if count > max_count:
            max_count = count
            best_word = word
    
    return best_word


print(most_letter_word(
    'she received an award for excellence in science','e'
))
# 'excellence'

print(most_letter_word(
    'she received an award for excellence in science','a'
))
# 'award'

print(most_letter_word(
    'I hope sophomore year comes soon','o'
))
# 'sophomore'

print(most_letter_word(
    'I hope sophomore year comes soon','s'
))
# 'sophomore'
