class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [2,4,-3,-1] -> [2]
        # [-4,2,1,7] -> [7]

        stack = []

        for a in asteroids:
            alive = True

            while a < 0 and stack and stack[-1] > 0 and alive == True:

                if abs(a) > stack[-1]:
                    stack.pop()
                
                elif abs(a) == stack[-1]:
                    stack.pop()
                    alive = False
                
                else:
                    alive = False

            if alive:
                stack.append(a)

        return stack