class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError("Negative numbers not allowed")

    print("Valid number")

except NegativeNumberError as e:
    print(e)
