class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sumDict =  {}

        for i, n in enumerate(nums):
            difference = target - n
            
            if difference in sumDict:
                return[sumDict[difference],i]
            

            sumDict[n] = i

        return False