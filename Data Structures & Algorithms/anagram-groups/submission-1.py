class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strDict = defaultdict(list)

        for s in strs:
            alph = [0] * 26
            for c in s: 
                alph[ord(c) - ord('a')] += 1

            strDict[tuple(alph)].append(s)

        
        return list(strDict.values())