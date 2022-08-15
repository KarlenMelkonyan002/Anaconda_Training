def sum_square():
    sum_ = 0
    for num in range(101):
        sum_ += num
    sum_sqr = sum_ ** 2
    return sum_sqr


def squares_sum():
    res = []
    num_lst = list(range(101))
    for i in num_lst:
        res.append(pow(num_lst[i], 2))
    square_sum = sum(res)
    return square_sum


def diff():
    return sum_square() - squares_sum()


print(diff())
