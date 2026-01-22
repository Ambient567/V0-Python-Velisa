# Write a function `raise_power(base, exponent)` that returns the result of
# base raised to the exponent using loops (do not use ** operator or math.pow).

def raise_power(base, exponent):
    prod = 1
    for num in range(exponent):
        prod *= base

    print(prod)



# Example:
raise_power(2, 5)  #-> 32
raise_power(4, 3)  #-> 64
raise_power(10, 4) #-> 10000
raise_power(7, 2)  #-> 49

