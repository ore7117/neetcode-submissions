class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l<=r:

            pivot = (l+r) // 2

            if nums[pivot] > target:
                # nums = l to pivot 
                r = pivot - 1
            
            elif nums[pivot]<target:
                # nums = pivot to r 
                l = pivot + 1    
                
            else:
                return pivot 
        
        return -1


        