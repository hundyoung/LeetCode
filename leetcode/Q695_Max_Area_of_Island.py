from typing import List
import numpy as np

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        def back_track(count,i,j):
            grid[i][j]=0
            for x,y in directions:
                if i+x<0 or i+x>=len(grid) or j+y<0 or j+y>=len(grid[i+x]):
                    continue
                if grid[i+x][j+y]==1:
                    count = back_track(count+1,i+x,j+y)
            return count
        max_count =0
        grid = np.array(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    count =back_track(1,i,j)
                    max_count = max(max_count,count)
        return max_count
s = Solution()

a = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(s.maxAreaOfIsland(a))


