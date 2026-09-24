class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        # BUCKET SORT
        # create a dictionary to store numbers and their frequencys
        # create a bucket array. the index will be the frequency, and the values will be the numbers that match the frequency. this list will store lists
        # return the list by K
        # worst case o(n). search full array at worst case, and lists with in the arrray make it o(n) + o(n)

        freqDict = {}

        bucket = [[] for i in range(len(nums)+1)]

        # add numbers and frequencys into map
        for n in nums: 
            if n not in freqDict:
                freqDict[n] = 1
            else: 
                freqDict[n] += 1 

        # add numbers, and frequencys into array

        for n, frequency in freqDict.items():
            bucket[frequency].append(n)
        
        # create array to store top k elements 

        result = []

        for frequency in range(len(bucket)-1, 0, -1):
            for num in bucket[frequency]:
                result.append(num)

            if len(result) == k:
                return result
         
