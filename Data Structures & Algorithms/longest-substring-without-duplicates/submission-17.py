class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        longest = 0
        l=0
        r=0
        while r<len(s):
            
            if s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            else:
                charSet.add(s[r])
                r+=1
            longest=max(longest,len(charSet))

        return longest
