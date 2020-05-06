from typing import List

import copy
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        self.total_p=0
        def back_track(index,current_p,left):
            if len(prob)-1-index>=left-1:
                if left==0:
                    for i in range(index,len(prob)):
                        current_p*=(1-prob[i])
                    self.total_p+=current_p
                else:
                    next=current_p*prob[index]
                    back_track(index+1,next,left-1)
                    next=current_p*(1-prob[index])
                    back_track(index+1,next,left)
        back_track(0,1,target)
        return self.total_p
s =Solution()
# print(s.probabilityOfHeads(prob =
# [0.3,0.4,0.5,0.6], target = 3))

print(s.probabilityOfHeads(prob =
                           [0.5, 0.5, 0.5, 0.5, 0.5], target = 1))


