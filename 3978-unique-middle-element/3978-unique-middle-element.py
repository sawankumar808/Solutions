class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:

        n=len(nums)
        mid=n//2
        value=nums[mid]
        count=0
        for ch in nums:
            if ch == value:
                count+=1
            
        if count==1:
            return True
        else:
            return False

        
            
            
    

            

                

            

            

