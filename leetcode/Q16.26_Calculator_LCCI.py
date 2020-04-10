class Solution:
    def calculate(self, s: str) -> int:
        def calculate(oper,n1,n2):
            n = 0
            if oper == '+':
                n = n1 + n2
            elif oper == '-':
                n = n1 - n2
            elif oper == '*':
                n = n1 * n2
            elif oper == '/':
                n = n1 // n2
            return n
        num_stack = []
        operation_stack = []
        operations={'-':0,'+':0,'*':1,'/':1}
        s = s.replace(' ','')
        s = s.replace('+','|+|')
        s = s.replace('-','|-|')
        s = s.replace('*','|*|')
        s = s.replace('/','|/|')
        s_group = s.split('|')
        for i in range(len(s_group)):
            char = s_group[i]
            if char=='':
                continue
            if char.isdigit():
                num_stack.append(int(char))
            else:
                if len(operation_stack)==0:
                    operation_stack.append(char)
                else:
                    if operations[char]>operations[operation_stack[-1]]:
                        operation_stack.append(char)
                    else:
                        pre_oper = operation_stack.pop(-1)
                        n2=num_stack.pop(-1)
                        n1 = num_stack.pop(-1)
                        num_stack.append(calculate(pre_oper,n1,n2))
                        operation_stack.append(char)
        if len(operation_stack)>0:
            pre_oper = operation_stack.pop(-1)
            n2 = num_stack.pop(-1)
            n1 = num_stack.pop(-1)
            num_stack.append(calculate(pre_oper, n1, n2))
        result = num_stack[0]
        for i in range(len(operation_stack)):
            oper = operation_stack[i]
            n2 = num_stack[i+1]
            result=calculate(oper,result,n2)
        return result
s =Solution()
print(s.calculate("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024"))
