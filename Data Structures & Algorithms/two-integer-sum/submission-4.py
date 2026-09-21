class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sumDict = dict()

        for i,n in enumerate(nums): 
            difference = target - n
            # return index that youre currently at + index of difference
            if difference in sumDict: 
                return [sumDict[difference], i]
            
            # mapping numbers to index [n: i]
            sumDict[n] = i

        return 