class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=s.strip()
        i=len(ans)-1
        count=0
        while i>=0 and ans[i]!=" ":
            count+=1
            i-=1
        return count
        