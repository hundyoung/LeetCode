class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n==1:
            return 0
        dp= [[float('inf') for j in range(n)] for i in range(n)]
        for i in range(n-1):
            dp[i][i] = 0
            dp[i][i+1] = i+1
        dp[-1][-1] = 0
        for l in range(2,n):
            for i in range(n-l):
                j = i+l
                dp[i][j] = min(dp[i][j], dp[i+1][j] + i+1)
                dp[i][j] = min(dp[i][j], dp[i][j-1] + j+1)
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j],max(dp[i][k-1],dp[k+1][j])+k+1)
        return dp[0][-1]
s = Solution()
print(s.getMoneyAmount(4))