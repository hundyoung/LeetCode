from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        # dp=[0]*len(gas)
        # dp[0]=total
        min_total = float('inf')
        min_i=0
        for i in range(0,len(gas)):
            left = (gas[i]-cost[i])
            total+=left
            if total<min_total:
                min_total=total
                min_i=i
            # dp[i] = max(dp[i-i]+left,left)
        if total<0:
            return -1
        else:
            return min_i+1 if min_i+1<=len(gas)-1 else min_i+1-len(gas)
            # return dp.index(max(dp))

s = Solution()
gas,cost =  [1,2],[2,1]
print(s.canCompleteCircuit(gas,cost))

