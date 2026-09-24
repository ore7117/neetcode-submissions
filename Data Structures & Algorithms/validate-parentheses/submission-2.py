class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ']':'[', '}':'{',')':'('
        }

        stack = []

    # check if the top of the stack stores the opening parentheses 
    # check the value of the hashmap 
    # also check if stack isnt empty
    # if the stack is empty, then return false 
    # if opening parentheses, append
    # return true if stack is empty
    # [()]

        for c in s: 
            if c in valid: 
                if len(stack) != 0 and stack[-1] == valid[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        
        return len(stack) == 0