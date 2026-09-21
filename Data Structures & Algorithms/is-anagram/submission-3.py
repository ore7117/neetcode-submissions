class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        anArray = [0] * 26

        if len(s) != len(t):
            return False

        for c in range (len(s)):
            anArray[ord(s[c]) - ord('a')] += 1
            anArray[ord(t[c]) - ord('a')] -= 1

        
        # check if anagram array is empty

        for n in anArray:
            if n != 0:
                return False

        return True


