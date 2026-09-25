class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        count =1 
        longest=1 
        if not nums:
            return 0

        for n in nums:
            #start of streak
            if n-1 not in numSet: 
                count =1 
            
                while(n+count) in numSet:
                    count +=1 

                longest = max(count,longest)
        
        return longest

                