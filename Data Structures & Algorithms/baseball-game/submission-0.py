class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations: 

            if o == '+':
                # record a new score that is sum of previous2 
                stack.append(stack[-1] + stack[-2])
            elif o == "C":
                # invalidate the previous score 
                stack.pop()
            elif o == 'D':
                stack.append(2 * stack[-1])
        
            else:
                stack.append(int(o))
        
        return sum(stack)