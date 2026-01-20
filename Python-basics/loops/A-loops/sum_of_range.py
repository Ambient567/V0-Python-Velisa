# Write `sum_of_range(n)`
# Print the sum of numbers from 1 to n.

def sum_of_range(n):
    sum = 0
    for x in range(n+1):
        sum += x

    print(sum)

sum_of_range(5)
# prints: 15
