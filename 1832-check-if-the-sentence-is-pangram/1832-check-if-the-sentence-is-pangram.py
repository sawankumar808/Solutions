class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ans= set(sentence)
        if len(ans)==26:
            return True 
        return False
        