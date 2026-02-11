# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


# Function that picks only prime numbers from a list
def pick_primes(numbers):
    result = []
    
    for number in numbers:
        if is_prime(number):
            result.append(number)
    
    return result


print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []
