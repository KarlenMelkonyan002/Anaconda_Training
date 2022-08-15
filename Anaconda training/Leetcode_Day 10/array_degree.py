def findShortestSubArray(nums):
    start, end, count = {}, {}, {}
    for i in range(len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 1
            start[nums[i]] = i
            end[nums[i]] = i
        else:
            count[nums[i]] += 1
            end[nums[i]] = i
        res = []
        degree = max((list(count.values())))
        for k, j in count.items():
            if degree == j:
                minimum = end[k] - start[k] + 1
                res.append(minimum)
        return min(res)


print(findShortestSubArray([[1, 2, 2, 3, 1]]))
