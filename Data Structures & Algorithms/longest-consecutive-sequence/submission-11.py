class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # base case 

        if not nums: 
            return 0

        numSet = set(nums)
        count = 1 
        longest = 1

        for n in numSet: 
            #define start of sequence
            if (n-1) not in numSet: 
                count = 1

                while (n+count) in numSet:
                    count += 1
            
            longest = max(count,longest)

        return longest