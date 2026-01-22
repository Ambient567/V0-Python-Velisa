# Write a function `filter_long_words(words)` that accepts a list of strings.
# The function should return a new list containing only the words that have
# less than 5 characters.

def filter_long_words(words):
    new_list = []

    for word in range(len(words)):
        if len(words[word]) < 5:
            new_list.append(words[word])

    print(new_list)

# Example:
filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]) #-> ['kale', 'cat', 'axe']
filter_long_words(["disrupt", "pour", "trade", "pic"]) #-> ['pour', 'pic']

