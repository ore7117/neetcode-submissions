class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1 # min speed 
        r = max(piles) # maxSpeed
        res = 0 

        while l<=r:
            pivot = (l+r)//2

            hours = 0 

            for pile in piles:

                hours += -(-pile // pivot)

            if hours > h:
                l = pivot + 1
            
            else:
                res = pivot 
                r = pivot -1
        
        return res


