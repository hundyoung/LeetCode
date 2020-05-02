from typing import List

import copy
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        count=0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if i==0 or j==0:
                    dp[i][j]=matrix[i][j]
                else:
                    if matrix[i][j]==1:
                        # if matrix[i-1][j-1]==1 and matrix[i][j-1]==1 and matrix[i-1][j]==1:
                        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                count+=dp[i][j]
        return count
s = Solution()
print(s.countSquares([
  [1,1,1],
  [1,1,1],
  [1,1,1]
]))

