# Palindrome Number
class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            # // は整数除算（小数点以下を切り捨てる）
            x //= 10
        return x == reversed_num or x == reversed_num // 10