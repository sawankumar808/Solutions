class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}
        for ch1, ch2 in zip(s, t):
            if ch1 in freq1 and freq1[ch1]!=ch2:
                return False
            if ch2 in freq2 and freq2[ch2]!=ch1:
                return False
            freq1[ch1]=ch2
            freq2[ch2]=ch1
        return True
        
            
        