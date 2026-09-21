class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freqDict = defaultdict(list)

        for s in strs: 
            freqArr = [0] * 26
            for c in s:
                freqArr[ord(c) - ord('a')] += 1
            freqDict[tuple(freqArr)].append(s)
            

        
        return list(freqDict.values())

    

