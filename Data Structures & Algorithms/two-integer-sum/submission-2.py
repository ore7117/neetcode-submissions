class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sumDict = dict()

        # add numbers to dictionary, with index 
        # if difference is not in dictionary, add until target is reached

        for i,n in enumerate(nums):
            difference = (target - n)
            
            if difference in sumDict:
                return [sumDict[difference], i]
            sumDict[n] = i

        return False