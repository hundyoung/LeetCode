from typing import List

import copy
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.dp = {}
        def back_track(left_needs,current_price):
            result=float('inf')
            for i in range(len(special)):
                items=special[i]
                can_buy=True
                left_needs_copy=copy.deepcopy(left_needs)
                for j in range(len(items)-1):
                    n = items[j]
                    if left_needs[j]-n<0:
                        can_buy=False
                        break
                    else:
                        left_needs_copy[j]-=n
                if can_buy:
                    if tuple(left_needs_copy) in self.dp:
                        a=self.dp[tuple(left_needs_copy)]
                    else:
                        a = back_track(left_needs_copy,current_price+items[-1])
                    result = min(result, a)
                b=current_price
                for j in range(len(left_needs)):
                    b+=left_needs[j]*price[j]
                result=min(result,b)
                key = tuple(left_needs)
                self.dp[key]=result
            return result
        return back_track(needs,0)
s = Solution()
print(s.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))
