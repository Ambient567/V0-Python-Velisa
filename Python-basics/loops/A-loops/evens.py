# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.

def evens(max_num):
    for x in range(max_num):
        if x % 2:
            print(x)

evens(11)
evens(8)

