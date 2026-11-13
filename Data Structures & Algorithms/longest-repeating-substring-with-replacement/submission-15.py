class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        alph = [0] * 26

        l = 0 
        r = 0 
        longest =0 

        while r<len(s):

            alph[ord(s[r]) - ord('A')] += 1

            if r-l+1 - max(alph) > k:
                alph[ord(s[l]) - ord('A')] -= 1
                l+=1

            longest = max(longest,r-l+1)
            r+=1
        
        return longest
        
        




