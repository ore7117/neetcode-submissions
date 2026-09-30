class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}
        
        for n in nums:
            if n in count:
                count[n]+= 1
            else:
                count[n]= 1
        

        majority = max(count, key=count.get)

        if count[majority] * 2 > len(nums):
            return majority
    
        return 0 