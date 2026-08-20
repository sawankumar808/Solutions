class Solution:
    def solve(self,nums, index,ans,output):
        if index>=len(nums):
            ans.append(output.copy())
            return 

        output.append(nums[index])

        self.solve(nums,index+1,ans, output)
        output.pop(len(output)-1)

        while index+1<len(nums) and nums[index]==nums[index+1]:
            index+=1

        self.solve(nums,index+1,ans, output)



    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        output=[]
        index=0
        self.solve(nums, index,ans, output)
        return ans


        