class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # set ? 

        # hash map where key = number, and value = frequency
        # HASH MAPS RETURN VALUE OF KEY! eg freqmap[key] = value

        freqMap = {}

        for n in nums: 
            if n in freqMap: 
                # increment count of key
                freqMap[n] += 1
            else: 
                # set key to value 1
                freqMap[n] = 1 
            # return k largest counts in freqMap 


            for values in freqMap.values():
                # return top k values 
                topk = sorted(freqMap, key=freqMap.get, reverse=True)[:k]

        return topk




            
            

