class Solution:
    def romanToInt(self, s: str) -> int:
        mapr = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
        n=len(s)
        
        ans=0
        for i in range(n-1):
            if mapr[s[i]]<mapr[s[i+1]]:
                ans-= mapr[s[i]]
            else: 
                ans+= mapr[s[i]]
        ans+=mapr[s[-1]]
        return ans


           
                
        