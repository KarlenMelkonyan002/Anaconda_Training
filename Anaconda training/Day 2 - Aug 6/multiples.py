def multiples(range_):
    sum_ = 0
    for num in range(1, range_):
        if num % 3 == 0 or num % 5 == 0:
            sum_ += num
    return sum_


print(multiples(10))
