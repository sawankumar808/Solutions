class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        #jaise hi muhje one milege mai count bada dung jesi hi one se alg milega mai count zero kar lunga or maximuma count return kar dunga
        count=0
        maxi=0 
        for ch in nums:
            if ch==1:
                count+=1
            else:
                count=0
            maxi=max(maxi, count)
        return maxi


    
        