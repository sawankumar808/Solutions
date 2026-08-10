class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        
        maxi=0
        for num in numset:
            if num-1 not in numset:
                startpoint=num
                count=1
                while startpoint +1 in numset:
                    count+=1
                    startpoint =startpoint+1
                maxi=max(maxi,count)
        return maxi


        