class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # want to store lists in the dictionary  so we can return a list
        freqDict = defaultdict(list)

        for s in strs: 
            alph = [0] * 26 
            for c in s:       
                alph[ord(c) - ord('a')] += 1

            freqDict[tuple(alph)].append(s)

        return list(freqDict.values())