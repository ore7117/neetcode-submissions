class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        if not nums:
            return 0 

        numSet = set(nums)
        longest = 0
        count = 1


        for n in numSet:
            # start of sequence.  
            if (n-1) not in numSet:
                count = 1
                # current sequence 
                while (n + count) in numSet: 
                    count += 1
            
                longest = max(count, longest)

        return longest
            