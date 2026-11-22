class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        pos=0
        for i,ch in enumerate(nums):
            if ch!=0:
                nums[pos]=ch
                pos+=1
        for i in range(pos,len(nums)):
            nums[i]=0
            
        
        



                
        