class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            if num not in count: 
                count[num] = 1
            else:
                count[num] += 1
        # make buckets for each possibl frequency
        freq = [[] for i in range (len(nums)+1)]
        # take number and frequency from map, and append it to the frequency array
        for num, frequency in count.items():
    
            freq[frequency].append(num)

        result = []

        for frequency in range(len(freq) -1, 0, -1):
            for num in freq[frequency]:
                result.append(num)

                if len(result) == k:
                    return result

        

