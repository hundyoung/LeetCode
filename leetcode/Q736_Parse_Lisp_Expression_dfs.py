class Solution:
    def evaluate(self, expression: str) -> int:
        # value_dict_list = []
        # value_dict = {}
        expression = expression.replace(')',' )')
        expression = expression.replace('(',' ( ')
        items = expression.split()
        # group_list = []
        # group = []
        result = -1
        def back_track(i,current_group:list):
            s = items[i]
            c_value_dict={}
            if i<len(items):
                if s==')':
                    operation = current_group.pop(0)
                    if operation=='add':
                        return i+1,current_group[0]+current_group[1]
                    elif operation=='mult':
                        return i+1,current_group[0]*current_group[1]
                    elif operation=='let':
                        for j in range(0,len(current_group)-1,2):
                            c_value_dict[current_group[j]]=current_group[j+1]
                        return i+1,c_value_dict[current_group[-1]]
                elif s=='(':
                    j,v = back_track(i+1,[])
                    current_group.append(v)
                else:
                    while items[i].isalpha() or items[i].isdigit():
                        current_group.append(items[i])
                        i+=1
                    j,v = back_track(i,current_group)
                    current_group.append(v)
                    j,v = back_track(j,current_group)

            else:
                global result
                result = current_group[0]
        back_track(0,[])
        return result





s = Solution()
print(s.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"))


