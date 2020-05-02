from typing import List

import math,copy
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        former_sum=0
        left=[]
        for n_str in prices:
            n_group=n_str.split('.')
            former_sum+=int(n_group[0])
            left.append(float('0.'+n_group[1]))
        target-=former_sum
        left.sort(reverse=True)
        result=0
        if target>len(left) or target<0:
            return '-1'
        for i in range(target):
            if math.ceil(left[i])==1:
                result+=(1-left[i])
            else:
                return '-1'
        for i in range(target,len(left)):
            result+=left[i]
        return str(('%.3f'%result))


s = Solution()
print(s.minimizeError(prices = ["0.700","2.800","4.900"], target = 8))

