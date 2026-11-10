class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        flat = []

        for m in matrix:
            
            for n in m:
                flat.append(n)
        

        l = 0
        r = len(flat)-1

        while l<=r:
            pivot = (l+r)//2

            if flat[pivot] < target:
                l = pivot+1

            elif flat[pivot] > target:
                r= pivot-1
            
            else:
                return True 
        
        return False
