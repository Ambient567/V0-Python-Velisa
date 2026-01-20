# Write a function:
# - If number is **even**, return **half**
# - If number is **odd**, return **double**

def number_change(n): 
    if n % 2 == 0: # check if even 
        return n // 2 
    else: # otherwise odd 
        return n * 2

print(number_change(6))   # 3
print(number_change(7))   # 14
print(number_change(16))  # 8
print(number_change(21))  # 42
