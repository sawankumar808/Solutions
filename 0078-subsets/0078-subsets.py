class Solution:
    def solve(self,nums, index,output,ans):
        if index>=len(nums):
            ans.append(output.copy())
            return

        output.append(nums[index])
        self.solve(nums, index+1,output,ans)
        output.pop(len(output)-1)

        

        self.solve(nums,index+1,output,ans)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        output=[]
        index=0
        self.solve(nums,index, output,ans)
        return ans

        