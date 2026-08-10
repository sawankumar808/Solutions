class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans=Counter(arr)
        seen=[]
        #return len(ans.values())==len(set(ans.values()))
        for ch in ans.values():
            if ch in seen :
                return False
            seen.append(ch)
        return True
        
        