def set_intersection(set1, set2):
    res = []
    for x in set1:
        if x in set2:
            res.append(x)
    return res


def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    if len(set1) < len(set2):
        return set_intersection(set1, set2)
    return set_intersection(set2, set1)


print(intersection([1, 2, 3], [3]))
