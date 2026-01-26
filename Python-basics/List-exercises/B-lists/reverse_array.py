# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

def reverse_array(arr):
    reversed_list = []
    for item in arr:
        reversed_list.insert(0, item)
    print(reversed_list)


# Example:
reverse_array(["zero", "one", "two", "three"]) # -> ['three', 'two', 'one', 'zero']
reverse_array([7, 1, 8])# -> [8, 1, 7]

