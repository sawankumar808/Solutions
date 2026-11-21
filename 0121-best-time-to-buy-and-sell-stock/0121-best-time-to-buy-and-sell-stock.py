class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #
        mini=float('inf')
        maxi=0
        for ch in prices:
            if ch<mini:
                mini=ch
            else:
                profit=ch-mini
                maxi=max(maxi, profit)
        return maxi
        