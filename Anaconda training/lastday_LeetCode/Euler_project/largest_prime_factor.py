import math


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def largestPrime(number):
    factors = [1]
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            if isPrime(i):
                number = number // i
                factors.append(i)
    return max(factors)


print(largestPrime(600851475143))
