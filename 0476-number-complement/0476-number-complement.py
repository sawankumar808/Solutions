class Solution:
    def findComplement(self, num: int) -> int:
        #bit ki length
        n=num.bit_length()
        #uska copy banana 
        mask= (1<< n)-1
        return num^mask
        