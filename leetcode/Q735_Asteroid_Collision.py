from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            ast = asteroids[i]
            if ast <0:
                while len(stack)>0:
                    if stack[-1]<=0 or stack[-1]>=-ast:
                        break
                    else:
                        stack.pop(-1)
                if len(stack) == 0:
                    stack.append(ast)
                else:
                    stack_top = stack[-1]
                    if stack_top==-ast:
                        stack.pop(-1)
                    elif stack_top<=0:
                        stack.append(ast)
            else:
                stack.append(ast)
        return stack

s =Solution()
print(s.asteroidCollision([10, 2, -5]))
