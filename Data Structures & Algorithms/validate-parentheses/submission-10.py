class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        valid = {

            ']':'[',
            '}':'{',
            ')':'('
        }

        for c in s:

            if c in valid: 
                if len(stack) > 0 and stack[-1] == valid[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack)==0