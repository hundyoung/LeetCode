import copy
class Solution:
    def evaluate(self, expression: str) -> int:
        value_dict_stack = []
        c_value_dict = {}
        expression = expression.replace(')',' )')
        expression = expression.replace('(',' ( ')
        items = expression.split()
        stack = []
        current_stack = []

        def is_number(s):
            try:
                int(s)
                return True
            except ValueError:
                pass
        for i in range(len(items)):
            s = items[i]
            if s=='(':
                if len(current_stack)>0 and current_stack[0]=='let':
                    for j in range(1, len(current_stack) - 1, 2):
                        if j+1<len(current_stack):
                            c_value_dict[current_stack[j]] = current_stack[j + 1]
                value_dict_stack.append(copy.deepcopy(c_value_dict))
                # c_value_dict={}

                stack.append(current_stack)
                current_stack=[]
            elif s==')':
                operation = current_stack.pop(0)
                c_value_dict = value_dict_stack.pop(-1)
                r = -1
                if operation == 'add' or  operation == 'mult':
                    a = int(current_stack[0]) if is_number(str(current_stack[0])) else int(c_value_dict[current_stack[0]])
                    b = int(current_stack[1]) if is_number(str(current_stack[1])) else int(c_value_dict[current_stack[1]])
                    if operation=='add':
                        r = a+b
                    else:
                        r= a*b
                elif operation == 'let':
                    for j in range(0, len(current_stack) - 1, 2):
                        c_value_dict[current_stack[j]] = current_stack[j + 1]
                    if is_number(str(current_stack[-1])):
                        r = current_stack[-1]
                    else:
                        r = c_value_dict[current_stack[-1]]

                    # pre_v_dict = value_dict_stack.pop(-1)
                    # pre_v_dict[current_stack[-1]]=c_value_dict[current_stack[-1]]
                pre_group = stack.pop(-1)
                pre_group.append(r)
                current_stack=pre_group
                # c_value_dict = value_dict_stack.pop(-1)

            else:
                current_stack.append(s)
        return int(current_stack[-1]) if is_number(str(current_stack[-1])) else int(c_value_dict[current_stack[-1]])


s = Solution()
print(s.evaluate("(let x0 -4 x1 2 x2 -1 x3 0 x4 -4 x5 2 x6 3 x7 -3 x8 0 x9 -1 (mult (let x0 -4 x3 4 x6 -1 x9 0 (mult (mult -4 -2) -4)) (add (add (let x0 1 x5 -4 (let x0 3 x6 -4 (let x0 0 x7 -5 (let x0 3 x8 -2 (mult x1 x3))))) (mult (add x6 x1) (mult -2 (mult x6 (let x0 -5 x8 -4 (mult (mult x8 x7) -4)))))) -3)))"))


