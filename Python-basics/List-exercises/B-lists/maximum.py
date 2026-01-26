# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(numbers):
    if len(numbers) == 0:
        return None

    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num

    print(max_value)


# Example:
maximum([5, 6, 3, 7])# -> 7
maximum([17, 15, 19, 11, 2])# -> 19
maximum([])# -> None

