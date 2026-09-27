class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        pos=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        while pos<n:
            nums[pos]=0
            pos+=1
                
        