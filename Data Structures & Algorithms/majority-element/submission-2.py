class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        
        for n in nums:
            if n not in count:
                count[n]=1
            else:
                count[n]+=1 

        m = max(count, key=count.get)
        

        if len(nums) // count[m]< 2: 
            return m

        return 0