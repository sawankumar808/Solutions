class Solution:
    def firstUniqChar(self, s: str) -> int:
        #for i in range(len(s)):
           # if s[i] not in s[:i] and s[i] not in s[i+1:]:
            #    return i
             #   break
       # return -1
        ans=Counter(s)
        for i, num in  enumerate(s):
            if ans[num]==1:
                return i
        return -1

        