class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        psum=defaultdict(int)
        psum={0:-1}
        currsum=0
        count=0

        for i in range(n):
            currsum+=nums[i]
            ans=currsum % k

            if ans in psum:
                if i-psum[ans]>1:
                    return True
            else:
                psum[ans]=i
        return False
            

        