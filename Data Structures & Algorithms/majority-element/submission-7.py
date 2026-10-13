class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freqDict = {}

        for n in nums:
            if n in freqDict:
                freqDict[n]+=1
            else:
                freqDict[n]=1 

        majority = max(freqDict, key=freqDict.get)

        if len(nums) // freqDict[majority] < 2:
            return majority 
        
        return 0
