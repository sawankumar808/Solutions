class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        stack=0

        for ch in s:
            if ch=='(':
                if stack>0:
                    ans=ans+ch
                stack+=1

                
            elif ch== ')':
                    stack-=1
                
                    if stack>0:
                        ans=ans+ch
                
        
        return ans

