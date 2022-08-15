def str_move(string, shifts):
    res = string[len(string) - shifts:] + string[0: (len(string) - shifts)]
    return res


print(str_move("hello", 3))
