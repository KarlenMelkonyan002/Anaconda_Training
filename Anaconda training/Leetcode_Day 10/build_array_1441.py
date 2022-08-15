def buildArray(target, n):
    res = []
    for elem in range(1, target[-1] + 1):
        if elem in target:
            res.append("Push")
        else:
            res.append("Push")
            res.append("Pop")
        if elem == target[-1]:
            break
    return res


print(buildArray([1, 3], 3))
