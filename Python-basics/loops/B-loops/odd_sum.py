# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

def odd_sum(max_num):
    sum = 0
    for x in range(max_num+1):
        if x % 2 != 0:
            sum += x
    print(sum)
    
# Example:
odd_sum(10) #-> 25  # 1 + 3 + 5 + 7 + 9
odd_sum(5)  #-> 9   # 1 + 3 + 5

