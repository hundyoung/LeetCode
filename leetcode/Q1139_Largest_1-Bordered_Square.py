from typing import List

import numpy as np
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        grid = np.asarray(grid)
        dp = [[[grid[i][j]]*2 for j in range(len(grid[i]))] for i in range(len(grid))]
        # dp = np.asarray(dp)
        # dp[0][0][0]=grid[0][0]
        # dp[0][0][1]=grid[0][0]
        for i in range(1,len(grid)):
            if grid[i][0]==1:
                dp[i][0][1]=dp[i-1][0][1]+1
        for j in range(1,len(grid[0])):
            if grid[0][j]==1:
                dp[0][j][0]=dp[0][j-1][0]+1
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    max_count=1
                    break
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                node = grid[i][j]
                if node==1:
                    dp[i][j][0]=dp[i][j-1][0]+1
                    dp[i][j][1]=dp[i-1][j][1]+1
                    for s in range(1,min(dp[i][j][0],dp[i][j][1])):
                        if dp[i][j-s][1]>s and dp[i-s][j][0]>s:
                            max_count = max(max_count,s+1)
        return max_count*max_count
s = Solution()
grid = [[0,0],[1,0]]
print(s.largest1BorderedSquare(grid))