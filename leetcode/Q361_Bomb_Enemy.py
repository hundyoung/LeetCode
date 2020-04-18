from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        dp = [[[0,1] for _ in range(len(grid[0]))]for _ in range(len(grid))]
        for i in range(len(grid)):
            e_count =0
            for j in range(len(grid[0])):
                if grid[i][j]=='W':
                    e_count=0
                elif grid[i][j]=='E':
                    e_count+=1
                dp[i][j][0]=e_count
        for j in range(len(grid[0])):
            e_count =0
            for i in range(len(grid)):
                if grid[i][j]=='W':
                    e_count=0
                elif grid[i][j]=='E':
                    e_count+=1
                dp[i][j][1]=e_count
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='0':
                    right=j
                    while right+1<len(grid[0]) and grid[i][right+1]!='W':
                        right=right+1
                    down=i
                    while down+1<len(grid) and grid[down+1][j]!='W':
                        down=down+1
                    count=max(count,dp[i][right][0]+dp[down][j][1])
        return count
s = Solution()
print(s.maxKilledEnemies([["0"],["E"],["0"],["W"]]))





