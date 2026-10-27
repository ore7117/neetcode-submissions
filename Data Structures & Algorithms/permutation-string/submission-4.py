class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        alph1 = [0] * 26 
        alph2 = [0] * 26
        l,r = 0,0

        for c in s1: 
            alph1[ord(c)-ord('a')] += 1

        while r<len(s2):

            alph2[ord(s2[r])-ord('a')] +=1

            if r-l+1 > len(s1):
                alph2[ord(s2[l]) - ord('a')] -=1
                l+=1
            
            if alph1 == alph2:
                return True
            
            r+=1
        
        return False
        

