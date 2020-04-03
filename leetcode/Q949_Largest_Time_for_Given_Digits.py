from typing import List

import itertools
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1
        result = ''
        for h0,h1,m0,m1 in  itertools.permutations(A):
            h = int(str(h0)+str(h1))
            m = int(str(m0)+str(m1))
            if h<24 and m<60:
                if max_time<int(str(h0)+str(h1)+str(m0)+str(m1)):
                    max_time=int(str(h0)+str(h1)+str(m0)+str(m1))
                    result=str(h0)+str(h1)+':'+str(m0)+str(m1)
        return result
s=Solution()
print(s.largestTimeFromDigits([2,0,6,6]))


