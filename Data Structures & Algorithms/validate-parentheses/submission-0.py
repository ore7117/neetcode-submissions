class Solution:
    def isValid(self, s: str) -> bool:
        # create a map that will validate closing parentheses 
        # create a stack that will store open parentheses 
        # iterate through s, if s is an opening parentheses, pop to the stack 
        # else, check if the stack isn't empty, and if the
        # if s 

        parenStack = []

        parenSet = {

            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        for c in s: 
            # check if character is a closing parentheses
            if c in parenSet:
                # if it is, then check if the top of the stack maps to an opening parentheses 
                if (len(parenStack)) != 0 and parenStack[-1] == parenSet[c]:
                    parenStack.pop()
                else: 
                    return False
            else: 
                parenStack.append(c)

        return len(parenStack) == 0 



