class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0 
        longest = 0 
        charSet = set()


        while r<len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r+=1
                longest = max(longest,r-l)
            else:
                charSet.remove(s[l])
                l+=1

        return longest
            
            
        