class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[ 0 for j in range(n) ]for i in range(m)]
        # print(dp)
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0]=1


        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]



        return dp[-1][-1]


s = Solution()
m = 3
n = 2
print(s.uniquePaths(m,n))