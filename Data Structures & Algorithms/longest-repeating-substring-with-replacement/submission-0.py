class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqDict = {} 
        res = 0 
        l = 0 
        r=0

        while r<len(s):
            if s[r] in freqDict:
                freqDict[s[r]] += 1
            else:
                freqDict[s[r]] = 1
            
            # length of window - highest character frequency
            # check if its greater than k
            while (r-l+1) - max(freqDict.values()) > k:
                freqDict[s[l]] -= 1
                l+=1 

            res = max(res,r-l + 1) 
            r+=1
        
        return res