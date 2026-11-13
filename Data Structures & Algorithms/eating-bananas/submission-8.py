class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        #[4,10,23,25]
        #[1,2,3,4] 5/2 
        l = 1 # min speed
        r = max(piles) # max sPeed 
        
        res = r

        while l<=r:
            pivot = (l+r) // 2

            hours = 0 

            for pile in piles:
                hours += -(-pile // pivot)

            if hours <= h:
                res = pivot 
                r = pivot - 1

            else:
                l = pivot + 1


        
        return res
        
        


