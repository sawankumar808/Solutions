class Solution:
    def maxDepth(self, s: str) -> int:
        level=0
        maxi=0

        for ch in s:
            if ch=='(':
                level+=1   
                maxi=max(maxi,level)

            if ch==')':
                level-=1
        return maxi