class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pmap=defaultdict(int)
        pmap[0]=1
        
        currsum=0
        ans=0

        for num in nums:

            if num%2!=0:
                val=1
            else:
                val=0

            currsum+=val
            target=currsum-k
            if target in pmap:
                ans+=pmap[target]
            pmap[currsum]+=1
        
        return ans


            

        