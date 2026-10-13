class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        maxP=0

        while r<len(prices):
            profit = prices[r]-prices[l]
            if prices[r]<prices[l]:
                l=r
                
                
                
            else:
                maxP=max(maxP,profit)
                
    
            r+=1
        return maxP
        