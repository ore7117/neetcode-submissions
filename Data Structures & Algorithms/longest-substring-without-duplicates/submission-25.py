class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        charSet = set()
        longest = 0 


        while r<len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r+=1 
            else:
                charSet.remove(s[l])
                l+=1
            
            longest = max(len(charSet),longest)


        
        return longest