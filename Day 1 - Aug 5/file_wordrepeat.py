def word_repeat(filename):
    dic = {}
    txt_file = open(filename, "r")
    data = txt_file.read().split()
    for elem in data:
        if elem in dic:
            dic[elem] += 1
        else:
            dic[elem] = 1
    return dic


print(word_repeat("test.txt"))
