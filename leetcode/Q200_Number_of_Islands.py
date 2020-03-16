from typing import List

import numpy as np
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid[i][j]= -1
                else:
                    grid[i][j]=0
        grid = np.array(grid)

        count =0
        def back_track(i,j):
            if grid[i][j]==-1:
                grid[i][j]=count
                if j - 1 >= 0:
                    back_track(i, j - 1)
                if j + 1 < len(grid[i]):
                    back_track(i, j + 1)
                if i + 1 < len(grid):
                    back_track(i + 1, j)
                if i - 1 >= 0:
                    back_track(i - 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==-1:
                    count+=1
                    back_track(i,j)

        return count
s = Solution()
print(s.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))
