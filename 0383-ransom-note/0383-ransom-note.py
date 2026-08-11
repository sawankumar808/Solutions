class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1=Counter(ransomNote)
        count2=Counter(magazine)
        if not count1-count2:
            return True
        return False



