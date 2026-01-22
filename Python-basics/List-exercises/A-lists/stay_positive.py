# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.

def stay_positive(numbers):
    new_list = []
    for num in range(len(numbers)):
        if numbers[num] > 0:
            new_list.append(numbers[num])

    print(new_list)

# Example:
stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
stay_positive([-11, -30]) #-> []

