class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hash map: map frequency array of alphabet with strings

        strMap = defaultdict(list)

        for s in strs: 
            # create frequency map for each character in string 
            alph = [0] * 26
            #
            for c in s:
                alph[ord(c) - ord('a')] += 1

            # convert to a tuple, since they are immutable. then append the string to the dictionary. 
            # a duplicate tuple will map to the same index
            strMap[tuple(alph)].append(s)



        return list(strMap.values())



