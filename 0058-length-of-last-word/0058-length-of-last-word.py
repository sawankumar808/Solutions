class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        n=len(s)
        i=n-1
        count=0
        while i>=0 and s[i]!=" ":
            count+=1
            i-=1
        return count

            

            
       
