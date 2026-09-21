class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqDict = defaultdict(list)

        for s in strs:
            anArray = [0] * 26 
            for c in s:
                anArray[ord(c) - ord('a')] += 1
            
            freqDict[tuple(anArray)].append(s)
    

        return list(freqDict.values())