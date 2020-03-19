from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for _ in range(len(T))]
        if len(T)==0:
            return 0
        tem_stack=[(len(T)-1,T[-1])]
        for i in range(len(T)-2,-1,-1):
            while len(tem_stack)>0:
                pre_i,pre_tem = tem_stack.pop(-1)
                cur_tem = T[i]
                if pre_tem<=cur_tem:
                    if len(tem_stack)==0:
                        result[pre_i]=0
                        tem_stack.append((i, cur_tem))
                        break
                else:
                    tem_stack.append((pre_i,pre_tem))
                    result[i]=tem_stack[-1][0]-i

                    tem_stack.append((i,cur_tem))
                    break
        return result
s = Solution()
print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))