def even_fib(lim):
    if lim < 2:
        return None
    even_1 = 0
    even_2 = 2
    sm = even_1 + even_2

    while even_2 <= lim:
        even_3 = 4 * even_2 + even_1
        if even_3 > lim:
            break
        even_1 = even_2
        even_2 = even_3
        sm += even_2
    return sm


print(even_fib(400))
