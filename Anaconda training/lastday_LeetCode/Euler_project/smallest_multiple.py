def isDivisible(num):
    for i in range(2, 21):
        if num % i != 0:
            return False
    return True


def solution():
    number = 20
    while True:
        if isDivisible(number):
            break
        number += 20
    print(number)


solution()
