class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freqDict = {}

        for n in nums:
            if n in freqDict:
                freqDict[n]+= 1
            else:
                freqDict[n] = 1


        majority = max(freqDict.values())

        if len(nums) // majority < 2:
            return max(freqDict, key=freqDict.get)
        
        return -1