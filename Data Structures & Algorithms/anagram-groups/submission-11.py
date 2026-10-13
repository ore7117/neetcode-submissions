class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = defaultdict(list)
        
        for s in strs:
            alph = [0]*26
            for c in s:
                alph[ord(c)-ord('a')] += 1
            
            group[tuple(alph)].append(s)
        
        
        return list(group.values())
        