class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        #isme muhje sabse phele 0 se k tak reverse karna or phir k se aage tak reverse karna hai
        n=len(nums)
        k=k%n
        self.reve(nums,0, n-1)# pura array reverse
        self.reve(nums,0,k-1)# k tak ka array reverse
        self.reve(nums, k, n-1)# k se aage tak ka array reverse
        

    def reve(self, nums, left , right):

        while left<right:
            nums[left], nums[right]=nums[right], nums[left]
            left += 1
            right -= 1
        
    