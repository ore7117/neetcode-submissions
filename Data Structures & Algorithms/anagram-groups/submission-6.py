class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqDict = defaultdict(list)

        for s in strs:
            alphabet = [0] * 26
            for c in s: 
                alphabet[ord(c) - ord('a')] += 1

            freqDict[tuple(alphabet)].append(s)

        
        return list(freqDict.values())