class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freqDict = {}
        l,r = 0,0
        longest = 0 
        while r<len(s):

            if s[r] not in freqDict:
                freqDict[s[r]] = 1
            else:
                freqDict[s[r]] +=1 
            
            if r-l+1 - max(freqDict.values()) > k:
                freqDict[s[l]] -= 1
                l+=1 
            
            longest = max(r-l+1, longest)
            r+=1
        
        return longest