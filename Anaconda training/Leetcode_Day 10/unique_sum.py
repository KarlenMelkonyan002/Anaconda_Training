def count_num(lst):
    """This function returns sum of unique(element appears once) element in list"""
    my_dict = {}
    for elem in lst:
        if elem in my_dict:
            my_dict[elem] += 1
        else:
            my_dict[elem] = 1
    sum_ = 0
    for key, val in my_dict.items():
        if val == 1:
            sum_ += key
    return sum_


