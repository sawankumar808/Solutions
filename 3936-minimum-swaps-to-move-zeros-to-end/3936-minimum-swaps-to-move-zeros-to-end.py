class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        #muhje to variable leke st or end mai cheack karna hai ki left side mai koi zero to nahi agr hai to to swwap karo ko aage badao or count bhi plus karo

        left=0
        right=len(nums)-1
        count=0
        while (left<right):
            if nums[left]==0 and nums[right]!=0:
                count+=1
                nums[left], nums[right]= nums[right], nums[left]
                left+=1
                right-=1
            elif nums[left] != 0:
                left += 1
            else:  # nums[right] == 0
                right -= 1
        return count

        