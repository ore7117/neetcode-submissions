class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value -> index

        for i,n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]


            prevMap[n] = i


# iterate value : index into hashmap one by one
# calculate difference. target - nums[n]
# if the target is in the hashmap already, return the key of where difference is in the map, and the index you are currently on in the array

