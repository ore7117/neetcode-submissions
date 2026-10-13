class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

              # create alpahbet arrays for each string 
        # populate the alphabet aray for s1
        # while r<len(s2), add r to the window 
        # sliding window of s1 length on right string. if it exceeds s1 length, then move the left pointer
        # if a match of len(s1 chars) is found, return true


        alph1, alph2 = [0]*26, [0]*26
        for c in s1: 
            alph1[ord(c) - ord('a')] += 1
        
        l = 0 
        r = 0 

        while r<len(s2):
            alph2[ord(s2[r]) - ord('a')] += 1 

            if r-l+1 > len(s1):
                alph2[ord(s2[l]) - ord('a')] -= 1 
                l+=1
            if alph1 == alph2: 
                return True
            
            r+= 1
        
        return False