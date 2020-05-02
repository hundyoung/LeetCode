class Solution:
    def waysToStep(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            current_sum=0
            for j in range(1,4):
                if i-j<0:
                    break
                else:
                    current_sum+=dp[i-j]
            dp[i]=current_sum%1000000007
        return dp[n]%1000000007
s = Solution()
print(s.waysToStep(900750))
