def isPalindrome(s):
    point1 = 0
    point2 = len(s) - 1

    while point1 < point2:
        if not s[point1].isalnum():
            point1 += 1
        elif not s[point2].isalnum():
            point2 -= 1
        else:
            if s[point1].lower() != s[point2].lower():
                return False
            else:
                point1 += 1
                point2 -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
