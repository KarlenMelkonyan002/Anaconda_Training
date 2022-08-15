def remove_duplicates(nums):
    moves = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[moves] = nums[i + 1]
            moves += 1
    return moves


print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
