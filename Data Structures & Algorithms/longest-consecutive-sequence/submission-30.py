class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        count = 1

        numSet = set(nums)

        for n in nums:
            # start of sequence
            if n-1 not in numSet:
                count = 1 
            # indicates a streak.
                while n+count in numSet:
                    count += 1
                longest = max(count,longest)
            
        return longest
