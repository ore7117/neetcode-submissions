class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   

        # dictionary that stores number and how many times it appears
        freqDict = {}

        # add numbers and frequency to dictionary
        for n in nums:
            if n not in freqDict: 
                freqDict[n] = 1
            else:
                freqDict[n] += 1

        # create buckets for each frequency
        # count(buckets) = count(n)
        freq = [[] for i in range(len(nums)+1)]

        # loop through each number and frequency
        for n, frequency in freqDict.items():
            # e.g freq[2].append(3)
            freq[frequency].append(n)

        # create array to store top k elements
        result = []
        
        # Start from the highest frequency in the array, and move backwards 
        for frequency in range(len(freq) -1, 0, -1):
            # loop through the numbers in the frequency array
            for num in freq[frequency]:
                result.append(num)

                # once k has ben reached, return
                if len(result) == k:
                    return result
