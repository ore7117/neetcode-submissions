class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        alph = [0] * 26

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            alph[ord(s[c]) - ord('a')] +=1
            alph[ord(t[c]) - ord('a')] -=1

        for n in alph: 
            if n != 0:
                return False
        
        return True
        