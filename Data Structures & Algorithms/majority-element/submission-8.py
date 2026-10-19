class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freqDict = {}

        for n in nums:
            if n not in freqDict:
                freqDict[n] = 1
            else:
                freqDict[n] += 1

        # len // max frequency > 2 = majority

        candidate = max(freqDict, key=freqDict.get)

        if len(nums) // freqDict[candidate] < 2:
            return candidate