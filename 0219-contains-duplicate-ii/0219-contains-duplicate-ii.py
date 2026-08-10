class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicti={}
        for i, ch in enumerate(nums):
            if ch in dicti:
                if i-dicti[ch]<=k:
                    return True
            dicti[ch]=i
        return False