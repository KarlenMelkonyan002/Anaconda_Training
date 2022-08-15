def containsDuplicate(nums):
    """Returns true if there is any duplicates,another solution is to use set.Just return len(nums) != len(set(nums))"""
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1

    for i in range(len(nums)):
        if dic[nums[i]] >= 2:
            return True
    return False


print(containsDuplicate([1, 2, 30, 30]))
