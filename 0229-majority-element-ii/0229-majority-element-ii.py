class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        freq={}
        n=len(nums)
        result=[]
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1


        for key,count in freq.items():
            if count>n//3:
                result.append(key)
        return result

        
        