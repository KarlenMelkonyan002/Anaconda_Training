def square(num):
    return num ** 2


def lst_square(func, lst):
    res = []
    for i in range(len(lst)):
        res.append(func(lst[i]))
    res.sort()
    return res


nums = [2, 9, 4, 11, 8]
print(lst_square(square, nums))
