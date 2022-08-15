def range_evens(start, end):
    res = []
    for num in range(start, end + 1):
        if num % 2 != 0:
            res.append(num)
    return tuple(res)


print(range_evens(3, 7))
