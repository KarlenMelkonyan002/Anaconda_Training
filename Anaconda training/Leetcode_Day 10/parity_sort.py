def sortArrayByParity(nums):
    """This  is function that moves all even elements in front of list I will try to improve it using quicksort"""
    return [n for n in nums if n % 2 == 0] + [n for n in nums if n % 2 == 1]
