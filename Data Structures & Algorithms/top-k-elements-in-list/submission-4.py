class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqDict = {}

        for n in nums: 
            
            if n in freqDict: 
                freqDict[n] += 1
            else: 
                freqDict[n] = 1

        topk = sorted(freqDict, key=freqDict.get, reverse = True)[:k]

        return topk