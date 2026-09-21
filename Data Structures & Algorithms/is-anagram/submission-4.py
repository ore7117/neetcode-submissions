class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # alphabet frequency map 
        alph = [0] * 26
        
        # cannot be anagram if lengths differ
        if len(s) != len(t):
            return False

        # map both strings, an array filled with zeroes, is a correct array
        for c in range (len(s)):
            alph[ord(s[c]) - ord('a')] += 1
            alph[ord(t[c]) - ord('a')] -= 1


        for n in alph: 
            if n != 0: 
                return False

        return True

        