class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #bf 

        nums.sort()
        #[2,2,3,4,6,7,8,9]
        count = 1
        longest = 1

        if not nums:
            return 0

        for n in range (len(nums) -1 ):
            # if equal
            if nums[n] == nums[n+1]: 
                continue
            # if not streak
            elif nums[n] != nums[n+1] - 1: 
                count = 1 
            else:
                count += 1
            
            longest = max(count,longest)

            
        return longest