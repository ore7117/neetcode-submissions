class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        
        for a in asteroids:

            alive = True

            while stack and a < 0 and stack[-1] > 0 and alive == True:

                if abs(a) < stack[-1]:
                    alive = False
                
                elif abs(a) > stack[-1]:
                    stack.pop()
                
                else:
                    stack.pop()
                    alive = False
            
            if alive:
                stack.append(a)
            
        return stack



        