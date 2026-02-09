# Write a function `max_object_value` that accepts a dictionary where:
# - keys are strings
# - values are numbers
# Return a list containing:
# - the key with the highest value
# - the highest value itself

def max_object_value(d):
    max_key = max(d, key=d.get)  # find key with max value
    return [max_key, d[max_key]]


print(max_object_value({"a": 5, "b": 2, "c": 6, "d": 7, "e": 4}))
# ['d', 7]

print(max_object_value({"lychee": 11, "rambutan": 13, "papaya": 9}))
# ['rambutan', 13]
