def findMaxConsecutiveOnes(nums):
    max_ones = 0
    curr_ones = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            curr_ones += 1
            max_ones = max(max_ones, curr_ones)
        else:
            curr_ones = 0
    return max_ones
