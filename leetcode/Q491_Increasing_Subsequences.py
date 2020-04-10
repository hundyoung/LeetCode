from typing import List

import copy
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results=[[]]
        final_results = set()
        for i in range(len(nums)):
            n = nums[i]
            to_add = []
            for j in range(len(results)):
                sub_array = copy.deepcopy(results[j])
                if len(sub_array)==0 or sub_array[-1]<=n :
                    sub_array.append(n)
                    to_add.append(sub_array)
            results+=to_add
        for i in range(len(results)):
            if len(results[i])>=2:
                final_results.add('|'.join(list(map(lambda x:str(x),results[i]))))
        results = []
        for s in final_results:
            s_group = s.split('|')
            results.append(list(map(lambda x:int(x),s_group)))
        return results
s =Solution()
print(s.findSubsequences([4, 6, 7, 7]))