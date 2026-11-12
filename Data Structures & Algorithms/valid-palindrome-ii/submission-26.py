class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(l,r):

            while l<r:

                if s[l].lower() == s[r].lower():
                    l+=1
                    r-=1
                
                else:
                    return False
                
            return True
        
        l = 0 
        r = len(s)-1

        while l<r:
            if s[l].lower() != s[r].lower():
                return isPalindrome(l,r-1) or isPalindrome(l+1,r)
            
            l+=1
            r-=1
            
        
        return True
