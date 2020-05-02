from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp=[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]==1:
                break
            else:
                dp[i][0]=1
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j]==1:
                break
            else:
                dp[0][j]=1
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[i])):
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
s = Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
