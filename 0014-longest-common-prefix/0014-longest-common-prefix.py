class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans = ""
        
        for i in range(len(strs[0])):        
            char = strs[0][i]                
            
            for j in range(len(strs)):        
                if i == len(strs[j]) or strs[j][i] != char: 
                    return ans                
            
            ans += char                      
            
        return ans