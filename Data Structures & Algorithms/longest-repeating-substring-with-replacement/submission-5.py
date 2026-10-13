class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqDict = {}
        longest = 0 
        l, r = 0, 0

        # aababaa k=1
        a:5
        b:2

        while r<len(s):
            if s[r] not in freqDict:
                freqDict[s[r]] = 1
            else:
                freqDict[s[r]] += 1

            if (r-l+1) - max(freqDict.values()) > k:
                freqDict[s[l]] -= 1
                l+=1 
            
            longest = max(longest,r-l+1)
            r+=1

        return longest





