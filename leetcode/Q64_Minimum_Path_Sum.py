from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[False]*len(grid[0]) for i in range(len(grid))]
        for j in range(len(grid[0])):
            dp[0][j]=sum(grid[0][:j+1])
        column_sum = 0
        for i in range(len(grid)):
            column_sum+=grid[i][0]
            dp[i][0]= column_sum

        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                dp[i][j]= min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])




        return dp[-1][-1]

s = Solution()
x=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(s.minPathSum(x))