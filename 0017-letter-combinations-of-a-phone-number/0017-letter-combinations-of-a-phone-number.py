class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz" ]
        index=0
        output=[]
        ans=[]
        self.solve(digits, index, mapping, output, ans)
        return ans
    
    def solve(self, digits, index,mapping, output, ans):
        if index>=len(digits):
            ans.append("".join(output))
            return

        value=int(digits[index])
        mappedString=mapping[value]

        for ch in mappedString:
            output.append(ch)
            self.solve(digits, index+1, mapping, output, ans)
        #backtracking
            output.pop()



                           