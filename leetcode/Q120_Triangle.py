from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==0:
            return 0
        dp=[[float('inf')]*len(triangle[i]) for i in range(len(triangle))]
        dp[0][0]=triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                v= triangle[i][j]
                if j-1>=0:
                    dp[i][j]=min(dp[i][j],dp[i-1][j-1]+v)
                if j<len(triangle[i-1]):
                    dp[i][j]=min(dp[i][j],dp[i-1][j]+v)
        return min(dp[-1])
s = Solution()
print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))

