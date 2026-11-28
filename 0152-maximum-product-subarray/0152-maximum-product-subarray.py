class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans=nums[0]
        multi=1
        left=1
        right=1
        n=len(nums)
        for i in range(n):
            if left==0:
                left=1
            if right==0:
                right=1
            
            left=left*nums[i]
            right=right*nums[n-1-i]
            ans=max(ans,left,right)
        return ans


        