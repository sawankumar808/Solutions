class Solution:
    def solve(self, nums, index, output, ans):
        if index >=len(nums):
            ans.append(output.copy())
            return
        currvalue=nums[index]
        output.append(currvalue)
        self.solve(nums, index+1, output, ans)

        output.pop()
        self.solve(nums, index+1, output, ans)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        output=[]
        self.solve(nums, 0, output, ans)
        return ans
        