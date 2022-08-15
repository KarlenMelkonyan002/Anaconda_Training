def palindrome_num(num):
    temp = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if temp == rev:
        return True
    else:
        return False


print(palindrome_num(10))
