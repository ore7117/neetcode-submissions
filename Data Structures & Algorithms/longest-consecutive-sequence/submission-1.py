class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        count = 1
        longest = 1

        if not nums:
            return 0 

        for n in range(len(nums) - 1):
            if nums[n] == nums[n+1]:
                continue
            elif nums[n+1] == nums[n] +1:
                count += 1 
            else: 
                count = 1
    
            longest = max(longest, count)

        return longest