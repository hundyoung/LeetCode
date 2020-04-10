class Solution:
    def calculate(self, s: str) -> int:
        stack_list=[]
        current_stack=[]
        s=s.replace(' ','')
        s=s.replace('+','|+|')
        s=s.replace('-','|-|')
        s=s.replace('(','|(|')
        s=s.replace(')','|)|')
        items = s.split('|')
        for i in range(len(items)):
            char = items[i]
            if char =='':
                continue
            if char=='(':
                stack_list.append(current_stack)
                current_stack=[]
            elif char==')':
                inner_result = current_stack[0]
                for j in range(1,len(current_stack),2):
                    operation = current_stack[j]
                    if operation=='+':
                        inner_result+=current_stack[j+1]
                    elif  operation=='-':
                        inner_result-=current_stack[j+1]
                current_stack = stack_list.pop(-1)
                current_stack.append(inner_result)
            else:
                if char.isdigit():
                    char=int(char)
                current_stack.append(char)
        if len(current_stack)>0:
            inner_result = current_stack[0]
            for j in range(1, len(current_stack), 2):
                operation = current_stack[j]
                if operation == '+':
                    inner_result += current_stack[j + 1]
                elif operation == '-':
                    inner_result -= current_stack[j + 1]
            return inner_result
        else:
            return current_stack[0]
s = Solution()
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
