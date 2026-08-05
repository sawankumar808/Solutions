class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pmap=defaultdict(int)
        pmap[0]=1
        currsum=0
        count=0

        for num in nums:
            currsum+=num

            if currsum % k in pmap:
                count=count+pmap[currsum % k]
            pmap[currsum % k]+=1
        return count


        