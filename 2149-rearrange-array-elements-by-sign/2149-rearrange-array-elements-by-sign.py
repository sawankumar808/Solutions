class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[0]*len(nums)
        posindex=0
        negindex=1
        for num in nums:
            if num>0:
                ans[posindex]=num
                posindex+=2
            else:
                ans[negindex]=num
                negindex+=2
        return ans