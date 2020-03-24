class Solution:
    def evaluate(self, expression: str) -> int:
        value_dict_list = []
        value_dict = {}
        expression = expression.replace(')',' )')
        expression = expression.replace('(',' ( ')
        items = expression.split()
        group_list = []
        group = []
        for i in range(len(items)):
            s = items[i]
            if s=='(' or s==')':
                if len(group)>0:
                    group_list.append(group)
                group=[]
                if len(value_dict)>0:
                    value_dict_list.append(value_dict)
                value_dict={}
            # elif s==')':
            #     operation = group.pop(0)
            #     if operation=='add':
            #         a = group.pop(0)
            #         b = group.pop(0)
            #         c = a+b

            else:
                group.append(s)
        return 1
s = Solution()
print(s.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"))


