class Solution:
    def solve(self, nums, index, output, ans):
        if index>=len(nums):
            ans.append(output.copy())
            return 
        ch=nums[index]
        output.append(ch)
        self.solve(nums, index+1, output, ans)
        output.pop()
        while index+1 < len(nums) and nums[index] ==nums[index+1]:
            index+=1
        self.solve(nums, index+1, output, ans)
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        ans=[]
        output=[]
        nums.sort()
        self.solve(nums, 0, output, ans)
        return ans
        