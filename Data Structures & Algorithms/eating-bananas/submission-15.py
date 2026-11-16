class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1 
        r = max(piles)

        res = r


        while l<=r:
            pivot = (l+r) // 2
            hours = 0 

            for p in piles:
                hours += -(-p // pivot)

            if hours <= h:
                res = pivot
                r = pivot - 1
            else: 
                l = pivot + 1

        

        return res
            




