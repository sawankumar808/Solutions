class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=[]
        for ch in s:
            if ch.isalnum():
                result.append(ch.lower())
        ans="".join(result)
            
        rstring=ans[::-1]
        if ans==rstring:
            return True
        else:
            return False
            

