class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0 
        l = 0 
        r = 1

        while r<len(prices):
            profit = prices[r]-prices[l]
            if prices[l]>prices[r]:
                prices[l]=prices[r]
            else: 
                r+=1
            maxProfit=max(maxProfit,profit)            
        return maxProfit

