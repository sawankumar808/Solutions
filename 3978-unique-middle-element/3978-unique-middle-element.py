class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:

        n=len(nums)
        mid=n//2
        value=nums[mid]
        fre=Counter(nums)
        if fre[value]>1:
            return False
        else:
            return True
            
            
    

            

                

            

            

