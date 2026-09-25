class Solution:
    def isValid(self, s: str) -> bool:

        valid = {
            ']':'[', '}':'{',')':'('
        }

        #create empty stack
        stack =[]

        # loop through list of parentheses 
        for c in s: 
            # if closing parentheses 
            if c in valid:
                # check if the top of the stack has an opening parentheses
                if len(stack) != 0 and stack[-1] == valid[c]:
                    # pop the opening parentheses from the top of stack
                    stack.pop()
                else:
                    # cant start with a closing prnths, and top of stack must be opening
                    return False
            
            else:
                stack.append(c)

        return len(stack) == 0

            