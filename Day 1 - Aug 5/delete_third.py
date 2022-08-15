def del_third(string):
    empty = ""
    for i in range(len(string)):
        if i % 3 != 2:
            empty += string[i]
    return empty


print(del_third("123456789"))
