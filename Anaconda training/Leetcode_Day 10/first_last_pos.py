def big_binary(nums, target):
    def leftBinary(lst, x):
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if x > lst[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def rightBinary(lst, x):
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if x > lst[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return right

    l, r = leftBinary(nums, target), rightBinary(nums, target)
    if l <= r:
        return l, r
    else:
        return [-1, -1]


print(big_binary([5, 7, 7, 8, 8, 10], 8))
