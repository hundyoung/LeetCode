from typing import List

import copy
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        def dfs(left,temp:list,max_i):
            if left==1 and len(temp)>0:
                result.append(temp)
            else:
                for i in range(2,left+1):
                    if i==n:
                        break
                    if left%i==0 and i>= max_i:
                        max_i=i
                        temp_copy = copy.deepcopy(temp)
                        temp_copy.append(i)
                        dfs(left//i,temp_copy,max_i)
        dfs(n,[],0)
        return result
s =Solution()
print(s.getFactors(1))