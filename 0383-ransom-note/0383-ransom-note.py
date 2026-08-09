class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1=Counter(ransomNote)
        count2=Counter(magazine)
        for char , count in count1.items():
            if count2[char]<count:
                return False
        return True



