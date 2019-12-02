from typing import List


class Solution:
    target = 0
    result = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.result = []
        self.digSum(0,[],candidates)
        return self.result

    def digSum(self,sum,temp:list,candidates:list):
        if sum<self.target and len(candidates)>0:
            ele = candidates.pop(0)
            current = temp.copy()
            currentCan = list(candidates)
            self.digSum(sum,current,currentCan)
            sum = sum+ele
            current = temp.copy()
            current.append(ele)
            currentCan = list(candidates)
            if sum == self.target:
                current.sort()
                if current not in self.result:
                    self.result.append(current)
            elif sum<self.target:
                self.digSum(sum,current,currentCan)
s =Solution()
print(s.combinationSum2([2,5,2,1,2],5))
