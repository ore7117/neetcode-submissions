class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0 
        r = len(numbers)-1

        while l<r:
            # conditions
            # if l+r = target, return l,r (add 1 cuz one indexed)
            # if l+r != target, we only have to move r-1, because it is ascending
            # increment l if no target is found at its index
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:
                r-=1        
            else:
                l+=1
        
        return []