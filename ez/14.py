# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # 最初の文字列を基準にする
        prefix = strs[0]
        
        for string in strs[1:]:
            # 文字列がprefixで始まらない限りprefixを短くする
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix