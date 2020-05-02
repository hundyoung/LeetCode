from typing import List

import math,copy
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        if len(prices)==0:
            return '-1'
        self.min_round=float('inf')
        prices=list(map(lambda x:float(x),prices))
        min_sum=0
        max_sum=0
        prices_sum = sum(prices)
        for n in prices:
            min_sum+=math.floor(n)
            max_sum+=math.ceil(n)
        if target<min_sum or target>max_sum:
            return '-1'
        elif target==min_sum:
            return str('%.3f' % (prices_sum-min_sum))
        elif target==max_sum:
            return str('%.3f' % (prices_sum-min_sum))

        def back_tack(temp:list):
            if len(temp)==len(prices):
                if  sum(temp)==target:
                    r=0
                    for i in range(len(temp)):
                        t=temp[i]
                        n = prices[i]
                        r+=abs(t-n)
                    self.min_round=min(self.min_round,r)
            else:
                temp_copy= copy.deepcopy(temp)
                temp_copy.append(math.floor(float(prices[len(temp)])))
                back_tack(temp_copy)
                temp_copy= copy.deepcopy(temp)
                temp_copy.append(math.ceil(float(prices[len(temp)])))
                back_tack(temp_copy)
        back_tack([])
        if self.min_round!=float('inf'):
            return str('%.3f' % self.min_round)
        else:
            return '-1'
s = Solution()
print(s.minimizeError(["20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000","20.000"]
,1000))

