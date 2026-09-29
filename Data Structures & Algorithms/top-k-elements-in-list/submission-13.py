class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        freqDict = {}

        bucket = [[]for i in range(len(nums)+1)]

        for n in nums:
            if n not in freqDict:
                freqDict[n] = 1
            else:
                freqDict[n] += 1

        for n, frequency in freqDict.items():
            bucket[frequency].append(n)
        
        topk = []

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                topk.append(num)
        
            if len(topk) == k:
                return topk
        
        return []