class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0 

        count = 1
        longest = 1

        numSet = set(nums)

        for n in numSet: 
            if (n-1) not in numSet:
                # start of sequence
                count = 1

                while (n+count) in numSet:
                    count += 1
            
            longest = max(count,longest)

        return longest
