class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sumDict =  {}

        for i, n in enumerate(nums):
            diff = target - n 

            if diff in sumDict: 
                return [sumDict[diff], i]   

            
            sumDict[n] = i
     