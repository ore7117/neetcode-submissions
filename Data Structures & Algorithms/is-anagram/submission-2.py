class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        alph = [0] * 26    

        if len(s) != len(t):
            return False

        
        for i in range (len(s)):
            alph[ord(s[i]) - ord('a')] += 1
            alph[ord(t[i]) - ord('a')] -= 1

        for n in alph:
            if n != 0:
                return False
    
        return True




        