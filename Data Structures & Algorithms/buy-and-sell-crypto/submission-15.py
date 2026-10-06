class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l=0
        r=1
        maxP=0
        p=0

        while r<len(prices):
            if prices[l]<prices[r]:
                p = prices[r]-prices[l]
            else:
            
                l = r
            
            r+=1
            maxP=max(p,maxP)


        return maxP