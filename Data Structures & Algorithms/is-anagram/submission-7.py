class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        alphabet = [0] * 26

        if len(s) != len(t):
            return False

        for c in range (len(s)): 
            alphabet[ord(s[c]) - ord('a')] += 1
            alphabet[ord(t[c]) - ord('a')] -= 1

        for n in alphabet: 
            if n != 0:
                return False

        return True
        


