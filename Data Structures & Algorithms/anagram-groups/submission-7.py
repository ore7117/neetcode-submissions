class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = defaultdict(list)

        for s in strs:
            a = [0] * 26
            for c in s:
                a[ord(c) - ord('a')] += 1

            group[tuple(a)].append(s)
        
        return list(group.values())