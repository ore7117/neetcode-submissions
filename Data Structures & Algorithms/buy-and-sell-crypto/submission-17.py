class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        l, r = 0,0
        profit = 0 

        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
            else:
                l=r
            
            maxProfit = max(profit,maxProfit)
        
            r+=1

        
        return maxProfit
        