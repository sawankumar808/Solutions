class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        h=len(haystack)
        if needle not in haystack:
            return -1

        for i in range(h-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1


