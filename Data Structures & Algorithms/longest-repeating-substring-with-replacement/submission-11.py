class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        #create frequency dictionary to keep track of characters
        #sliding window 
        #append to freqDict
        #if length of window - max frequency > k 
        #there are not enough k's to replace, move window right
        #keep track of longest window

        freqDict = {}
        l,r = 0,0
        longest = 0 


        while r<len(s):
            if s[r] not in freqDict: 
                freqDict[s[r]] = 1
            else:
                freqDict[s[r]] += 1

            if (r-l+1) - max(freqDict.values()) > k:
                freqDict[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)
            r+=1 
        return longest
