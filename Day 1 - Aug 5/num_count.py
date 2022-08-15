def count_num(lst):
    my_dict = {}
    for elem in lst:
        if elem in my_dict:
            my_dict[elem] += 1
        else:
            my_dict[elem] = 1

    for key, val in my_dict.items():
        print(f"{key}: {val}")


my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
count_num(my_list)
