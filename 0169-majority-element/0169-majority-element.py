class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        maxifreq=0
        maxikey=-1
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1
            
        for ch in freq:
            currkey=ch
            currkeyfre=freq.get(ch)
            if currkeyfre>maxifreq:
                maxifreq=currkeyfre
                maxikey=currkey

        return maxikey
           

      

        