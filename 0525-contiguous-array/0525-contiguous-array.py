class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        currsum=0
        maxi=0
        pmap={0:-1}
        for i,num in enumerate(nums):
            if num==1:
                currsum+=1
            else:
                num==0
                currsum+=-1
                
            if currsum in pmap:
                length=i-pmap[currsum]
                maxi=max(maxi,length)
            else:
                pmap[currsum]=i
        return maxi



        