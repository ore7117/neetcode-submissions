class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freqDict = defaultdict(list)

        for s in strs:
            alph = [0] * 26 
            for c in s: 
                alph[ord(c) - ord('a')] += 1
            freqDict[tuple(alph)].append(s)

        return list(freqDict.values())