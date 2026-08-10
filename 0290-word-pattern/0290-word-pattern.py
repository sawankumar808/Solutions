class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ans=s.split()
        map1={}
        map2={}
        if len(pattern)!=len(ans):
            return False
        for i in range(len(pattern)):
            if pattern[i] in map1 and map1[pattern[i]]!=ans[i]:
                return False
    
            if ans[i] in map2 and map2[ans[i]]!=pattern[i]:
                return False
            map1[pattern[i]]=ans[i]
            map2[ans[i]]=pattern[i]
        return True

