def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution():
    first_prime = 2
    first_index = 0
    while first_index < 10000:
        first_prime += 1
        if isPrime(first_prime):
            first_index += 1
    return first_prime


print(solution())
