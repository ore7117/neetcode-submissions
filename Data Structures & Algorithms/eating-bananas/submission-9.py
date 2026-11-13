class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        res = r  

        while l<=r:
            pivot = (l+r) // 2

            hours = 0 

            for pile in piles:

                hours += -(-pile // pivot)

            if hours > h:
                l = pivot + 1
            
            else:
                res = pivot
                r = pivot - 1
               

        return res
            




    

        