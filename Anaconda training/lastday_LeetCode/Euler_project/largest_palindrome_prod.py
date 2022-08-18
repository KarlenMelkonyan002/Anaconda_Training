def isPalindrome(num):
    return str(num) == str(num)[::-1]


def largestPalindrome():
    max_palindrome = 1
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if isPalindrome(i * j) and i * j > max_palindrome:
                max_palindrome = i * j
            elif i * j < max_palindrome:
                break
    return max_palindrome


print(largestPalindrome())
