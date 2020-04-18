class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            for j in range(0,i):
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j])
        return dp[n]
s = Solution()
print(s.integerBreak(3))
