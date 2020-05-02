class Solution:
    def divisorGame(self, N: int) -> bool:
        if N ==1:
            return False
        dp= [False]*(N+1)
        dp[1]=False
        for i in range(2,len(dp)):
            dp[i] = False
            for j in range(1,i):
                if i%j==0 and dp[i-j]==False:
                    dp[i]=True
                    break
        return dp[N]
s = Solution()
print(s.divisorGame(3))
