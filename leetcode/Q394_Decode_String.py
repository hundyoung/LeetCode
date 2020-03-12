class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!= ']':
                stack.append(char)
            else:
                temp=[]
                while len(stack):
                    stack_top = stack.pop(-1)
                    if stack_top=='[':
                        times = []
                        while len(stack)>0:
                            digit = stack.pop(-1)
                            if digit.isdigit():
                                times.insert(0,digit)
                            else:
                                stack.append(digit)
                                break
                        stack += temp*int(''.join(times))
                        break
                    else:
                        temp.insert(0,stack_top)
        return ''.join(stack)


s = Solution()
print(s.decodeString('100[leetcode]'))
