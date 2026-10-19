class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0 
        l,r=0,0

        while r<len(prices):
            profit = prices[r] - prices[l]
            
            if prices[r] < prices[l]:
                l+=1
            else:
                r+=1
                maxP = max(profit,maxP)

        return maxP