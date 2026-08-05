class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        curr_sum=0
        count=0
        pmap = defaultdict(int)
        pmap[0]=1
        for num in nums:
            curr_sum+=num
            if curr_sum-k in pmap:
                count+=pmap[curr_sum-k]

            pmap[curr_sum]+=1
        return count
        