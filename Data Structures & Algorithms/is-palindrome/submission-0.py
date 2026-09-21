class Solution:
    def isPalindrome(self, s: str) -> bool:

        lc = s.lower()
        cleaned = []

        for c in lc: 
            if c.isalnum():
                cleaned.append(c)

        s = "".join(cleaned) 

        return s == s[::-1]   


  