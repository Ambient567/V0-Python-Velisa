# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

def sum_up_to(num):
    sum = 0
    for x in range(num+1):
        sum += x

    print(sum)

# Example:
sum_up_to(4)  #-> 10
sum_up_to(5)  #-> 15
sum_up_to(2)  #-> 3

