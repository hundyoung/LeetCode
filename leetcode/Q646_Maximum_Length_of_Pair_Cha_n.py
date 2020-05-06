from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs)==0:
            return 0
        pairs=sorted(pairs,key=lambda x:x[0])
        dp=[1]*len(pairs)
        for i in range(1,len(pairs)):
            l,r=pairs[i]
            for j in range(i-1,-1,-1):
                pre_l,pre_r=pairs[j]
                if pre_r<l:
                    dp[i]=max(dp[i],dp[j]+1)
        return dp[-1]
s = Solution()
print(s.findLongestChain([[3,4],[2,3],[1,2]]))

