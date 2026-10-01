class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create value/frequency map
        freqDict = {}

        # create bucket where indexes are frequencys, and the value of the index is a list of all the numbers that correspond to that frewuency
        bucket = [[]for i in range(len(nums)+1)]

        # add to frequency dictionary 

        for n in nums:
            if n not in freqDict: 
                freqDict[n]=1
            else:
                freqDict[n]+=1

        # append the frequency dictionary to the bucket

        for n, frequency in freqDict.items():
            bucket[frequency].append(n)
        
        # create an array that stores topk elements
        # the bucket we created stores the highest frequencies at the end so we need to traverse backwards

        topk = []

        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                topk.append(n)
        
            if len(topk) == k:
                return topk 

        return []
            


        