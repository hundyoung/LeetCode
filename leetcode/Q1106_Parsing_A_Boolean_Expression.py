class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        current_stack = []
        current_operation = ''
        operation_stack = []
        stacks = []

        for i in range(len(expression)):
            s = expression[i]
            if s==')':
                r = current_stack.pop(0)
                if current_operation=='!':
                    r = not r
                else:
                    for item in current_stack:
                        if current_operation == '&':
                            r = r and item
                        elif current_operation == '|':
                            r = r or item
                current_stack = stacks.pop(-1)
                current_stack.append(r)
                current_operation = operation_stack.pop(-1)
            elif s=='&' or s=='|' or s=='!':
                operation_stack.append(current_operation)
                current_operation = s
                stacks.append(current_stack)
                current_stack = []
            else:
                if s=='f' or s=='t':
                    current_stack.append(True) if s=='t' else current_stack.append(False)
        return current_stack[-1]

s = Solution()
print(s.parseBoolExpr("!(f)"))





