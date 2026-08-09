class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        ans=set(nums1)
        ans1=set(nums2)
        for ch in ans:
            if ch in ans1:
                result.append(ch)
        return result
        