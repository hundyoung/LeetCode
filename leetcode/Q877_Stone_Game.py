from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[[0,0]for _ in range(len(piles))]for _ in range(len(piles))]
        dp[0][len(piles)-1]=[0,float('-inf')]
        for i in range(len(piles)):
            dp[i][i]=[piles[i],0]
        for k in range(1,len(piles)):
            for i in range(len(piles)-k):
                j = i+k
                if i==0 and j==len(piles)-1:
                    continue
                if dp[i+1][j][1]>dp[i][j-1][1]:
                    dp[i][j][0]=dp[i+1][j][1]
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0]=dp[i][j-1][1]
                    dp[i][j][1] = dp[i][j-1][0]
        return dp[-1][-1][0]>=dp[-1][-1][1]

s = Solution()
print(s.stoneGame([5,3,4,5]))
