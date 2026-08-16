class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                sum = ast + stack[-1]

                if sum > 0:
                    ast = 0
                elif sum < 0:
                    stack.pop()
                else:
                    ast = 0
                    stack.pop()
            if ast:
                stack.append(ast)
        
        return stack
        