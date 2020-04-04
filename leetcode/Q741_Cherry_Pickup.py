from typing import List
import numpy as np
import copy
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dynamic_programming():
            dp = [[0 for i in range(len(grid[j]))] for j in range(len(grid))]
            dp[0][0]=grid[0][0]
            grid[0][0] = 0
            for i in range(1,len(dp)):
                if grid[i][0]!=-1:
                    dp[i][0] = dp[i-1][0]+grid[i][0]
                    # grid[i][0] = 0
            for j in range(1,len(dp[0])):
                if grid[0][j]!=-1:
                    dp[0][j] = dp[0][j-1]+grid[0][j]
                    # grid[0][j]=0
            dp = np.asarray(dp)
            for i in range(1,len(dp)):
                for j in range(1,len(dp[i])):
                    for k in range(2):
                        if grid[i][j]!=-1:
                            if dp[i][j-1]<dp[i-1][j]:
                                if grid[i-1][j]!=-1:
                                    dp[i][j]=dp[i][j]+dp[i-1][j]+grid[i][j]
                                    dp[i - 1][j]=0
                                    grid[i-1][j]=0
                            else:
                                if grid[i][j-1]!=-1:
                                    dp[i][j] = dp[i][j] +dp[i][j-1] + grid[i][j]
                                    dp[i][j - 1]=0
                                    grid[i][j-1]=0
                                elif grid[i-1][j]!=-1:
                                    dp[i][j]=dp[i][j]+dp[i-1][j]+grid[i][j]
                                    dp[i - 1][j]=0
                                    grid[i-1][j]=0
            grid[-1][-1]=0
            return dp[-1][-1]
        grid = np.asarray(grid)
        if len(grid)>0:
            if len(grid[0])>0:
                block_grid = copy.deepcopy(grid)
                block_grid[0][0]=1
                for i in range(1,len(block_grid)):
                    if block_grid[i][0]!=-1:
                        block_grid[i][0]= block_grid[i-1][0]
                for j in range(1, len(block_grid[0])):
                    if block_grid[0][j]!=-1:
                        block_grid[0][j]=block_grid[0][j-1]

                for i in range(1,len(block_grid)):
                    for j in range(1,len(block_grid[i])):
                        if block_grid[i][j]!= -1 and (block_grid[i-1][j]!=-1 or block_grid[i][j-1]!=-1):
                            block_grid[i][j]=1
                        else:
                            block_grid[i][j]=-1
                if block_grid[-1][-1]==-1:
                    return 0
                result = dynamic_programming()
                return result
            else:
                return 0
        else:
            return 0
s= Solution()
grid =[[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]
print(s.cherryPickup(grid))






