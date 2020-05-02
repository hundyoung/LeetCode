class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if K==0:
            return 0
        dp = [[float('inf')]*(1+K) for _ in range(N+1)]
        for l in range(N+1):
            dp[l][1]=l
        for k in range(K+1):
            dp[1][k]=1
        for i in range(2,N+1):
            for j in range(2,K+1):
                if N-i>=0:
                    dp[i][j]=min(dp[i][j],max(dp[i-1][j-1],dp[i][N-i]))+1
                else:
                    dp[i][j] =min(dp[i][j],dp[i][j-1])+1
        return dp[N][K]
s = Solution()
print(s.superEggDrop(2,6))
