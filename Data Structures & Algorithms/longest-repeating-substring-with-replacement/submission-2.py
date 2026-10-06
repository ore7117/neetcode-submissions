class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        alph = [0] * 26
        l,r = 0,0
        longest = 0 

        while r<len(s):
            alph[ord(s[r]) - ord('A')] += 1


            if r-l+1 - max(alph) > k:
                alph[ord(s[l])- ord('A')] -= 1
                l+=1 
            
                      
            longest = max(r-l+1,longest)
            r+=1 
        
        return longest
    
        