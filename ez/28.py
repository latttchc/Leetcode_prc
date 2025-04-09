# Find the Index of the First Unique Character in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1

        needle_length = len(needle)
        haystack_length = len(haystack)

        for i in range(haystack_length - needle_length + 1):
            if haystack[i : i+needle_length] == needle:
                return i

        return -1