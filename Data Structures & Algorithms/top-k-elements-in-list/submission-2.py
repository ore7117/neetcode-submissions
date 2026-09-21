class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}

        for n in nums: 
            
            if n in freqMap:
                freqMap[n] += 1
            else: 
                freqMap[n] = 1

        # sort the frequency map keys
        # get their values
        # python will sort the values in ascendning order by default
        # we want descending order, so we reverse=true
        #slice list by k --> [:k]
            # [1,1,1,2,3,3]
            # keys = [1,2,3]
            # get = [3,1,2] 
            # python auto sort [1,2,3]
                # corresponding keys after sort [2,3,1]
            # reverse [1,3,2]
            # slice reverse by k --> [1,3]] (will return keys)

        topk = sorted(freqMap, key=freqMap.get, reverse=True)[:k]

        return topk

        
       