class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [0]*(n+1)
        coins=[1,5,10,25]
        dp[0]=1
        for coin in coins:
            for i in range(1,n+1):
                if i-coin>=0:
                    dp[i]+=(dp[i-coin])
        return dp[-1]%1000000007
s = Solution()
print(s.waysToChange(10))
