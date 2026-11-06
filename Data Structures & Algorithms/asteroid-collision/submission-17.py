class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
      
        stack = []

      # Stack simulation: collisions only occur when stack top > 0 and incoming asteroid < 0. Recheck with while for chain reactions; compare abs sizes, pop smaller, remove both if equal. O(n) time, O(n) space.


        for a in asteroids:
            alive = True

            while stack and alive == True and a < 0 and stack[-1] > 0:

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
    