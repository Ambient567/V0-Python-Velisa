# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.

def total(numbers):
    sum = 0
    for num in range(len(numbers)):
        sum += numbers[num]

    print(sum)

# Example:
total([3, 2, 8]) #-> 13
total([-5, 7, 4, 6]) #-> 12
total([7]) #-> 7
total([]) #-> 0

