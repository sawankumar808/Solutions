class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        #muhje jab tak chekc karne hai ki ele same hai
        i=0# ye zero index hai par ahi
        for j in range(len(nums)):# n tak chalege 
            if nums[i]!=nums[j]: # jais hi koi un same number milege i=0 par hai or unsame j=2 
                i+=1 # i plus ho jyga or, i hogya ab 1
                nums[i]=nums[j] #i ke index par vo unsame number aa jyga, nums[1]par dal do 2 
        return i+1 #i+1 isliye return karte hai kyuki count batana ho hai 
            

        


        