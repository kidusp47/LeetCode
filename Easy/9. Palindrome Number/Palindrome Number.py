# def isPalindrome(x:int):
#     """Return True if x is a palindrome."""
#     if x < 0:
#         return False
#     num = list(map(int, str(x)))
#     for i in range(len(num)//2):
#         if num[i] != num[-i-1]:
#             return False
#     return True
#
# print(isPalindrome(10))

# a Genius method i saw

def isPalindrome(x:int):
    """Return True if x is a palindrome."""
    if x < 0:
        return False
    rev =0
    num = x
    while num != 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev == x

print(isPalindrome(1))