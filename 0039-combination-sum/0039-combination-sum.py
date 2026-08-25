class Solution:
    def solve(self,candidates, target, index, ans, output):
        if target==0:
            ans.append(output.copy())
            return
        if index>= len(candidates):
            return
        if target<0:
            return
        output.append(candidates[index])
        self.solve(candidates, target-candidates[index], index, ans, output)
        output.pop()
        self.solve(candidates, target, index+1, ans, output)



    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        index=0
        ans=[]
        output=[]
        self.solve(candidates, target, index, ans, output)
        return ans

           