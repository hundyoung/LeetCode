class Solution:
    def numTrees(self, n: int) -> int:
        if n<1:
            return 0
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][i]=1
        for l in range(1,n+1):
            for i in range(1,n+1):
                j=i+l
                if j>=n+1:
                    break
                if l==1:
                    dp[i][j] = dp[i][j-1] + dp[i+1][j]
                else:
                    for k in range(i,j+1):
                        if k==i:
                            dp[i][j]=dp[i][j]+dp[k+1][j]
                        elif k==j:
                            dp[i][j]=dp[i][j]+dp[i][k-1]
                        else:
                            dp[i][j]=dp[i][j]+dp[i][k-1]*dp[k+1][j]
        return dp[1][-1]
s = Solution()
print(s.numTrees(4))