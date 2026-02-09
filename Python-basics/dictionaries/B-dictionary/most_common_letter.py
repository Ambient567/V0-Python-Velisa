# Write a function `most_common_letter` that accepts a string as an argument.
# The function should return the character that appears most frequently in the string.
# Assume there are no ties and the string contains only lowercase letters.

def most_common_letter(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    # Find the character with the maximum count
    max_char = max(count_dict, key=count_dict.get)
    return max_char


print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'
