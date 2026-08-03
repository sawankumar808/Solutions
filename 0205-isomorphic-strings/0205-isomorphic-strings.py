class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:           
        freq1={}
        freq2={}
        for i in range(len(s)):
            fs=s[i]
            ft=t[i]

            if fs in freq1:
                if freq1[fs]!=ft:
                    return False
            else:
                freq1[fs]=ft
            if ft in freq2:
                if freq2[ft]!=fs:
                    return False
            
            freq2[ft]=fs

        return True
        
            
        