class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #sabse phele sum nikalete huwe chale or maxi ko update karte huwe chale
        maxi=-float('inf')
        print(maxi)
        count=0
        for i in range(len(nums)):
            count=count+nums[i]
            maxi=max(maxi,count)

            #agr abhi tak sum minus mai hai to zero se kardo
            if count<0:
                count=0
        return maxi

        