class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini=float('inf')
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:#agr prices bada hai pichle din se to unka
            #diffrence nikal lo or profit mai addkarte rhe usko
                diff = prices[i] - prices[i - 1]
                profit = profit + diff 

        return profit


        