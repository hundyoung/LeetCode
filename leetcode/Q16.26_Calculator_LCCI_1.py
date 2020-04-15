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
        num_stack = [[]]
        operation_stack = [[]]
        c_num_stack = []
        c_operation_stack = []
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
                c_num_stack.append(int(char))
            else:
                if len(c_operation_stack)==0:
                    c_operation_stack.append(char)
                else:
                    if operations[char]>operations[c_operation_stack[-1]]:
                        temp=c_num_stack.pop(-1)
                        num_stack.append(c_num_stack)
                        operation_stack.append(c_operation_stack)
                        c_operation_stack=[]
                        c_operation_stack.append(char)
                        c_num_stack=[temp]
                    elif operations[char] == operations[c_operation_stack[-1]]:
                        c_operation_stack.append(char)
                    else:
                        r = c_num_stack[0]
                        for i in range(len(c_operation_stack)):
                            r = calculate(c_operation_stack[i],r,c_num_stack[i+1])
                        c_operation_stack=operation_stack.pop(-1)
                        c_operation_stack.append(char)
                        c_num_stack=num_stack.pop(-1)
                        c_num_stack.append(r)
        # if len(c_operation_stack)>0:
        while len(operation_stack)>0:
            r = c_num_stack[0]
            for i in range(len(c_operation_stack)):
                r = calculate(c_operation_stack[i], r, c_num_stack[i + 1])
            c_operation_stack = operation_stack.pop(-1)
            c_num_stack = num_stack.pop(-1)
            c_num_stack.append(r)
        r = c_num_stack[0]
        for i in range(len(c_operation_stack)):
            r = calculate(c_operation_stack[i], r, c_num_stack[i + 1])
        return r
s =Solution()
print(s.calculate("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024"))
# print(s.calculate(" 3+5 / 2 "))
