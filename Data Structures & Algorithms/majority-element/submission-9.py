class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freqDict = {}

        for n in nums:
            if n not in freqDict:
                freqDict[n] = 1
            else:
                freqDict[n] += 1
        

        m = max(freqDict.values())

        if len(nums) // 2 < m:
            return max(freqDict, key= freqDict.get)
        
    
        return -1