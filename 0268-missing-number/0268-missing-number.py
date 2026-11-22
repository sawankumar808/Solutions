class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        totalsum=n*(n+1)//2
        count=0
        for i in range(n):
            count+=nums[i]
        return totalsum-count