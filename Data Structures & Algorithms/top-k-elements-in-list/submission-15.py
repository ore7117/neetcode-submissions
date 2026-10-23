class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[]for i in range(len(nums)+1)]

        freqDict = {}

        for n in nums:
            if n not in freqDict:
                freqDict[n] = 1
            else:
                freqDict[n] += 1
        
        for n,frequency in freqDict.items():
            bucket[frequency].append(n)
        
        res = []

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
            
            if len(res) == k:
                return res
        
        return []