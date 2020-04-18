class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        dp = [0]*(n)
        dp[0]=10
        for i in range(1,n):
            com=9
            for j in range(9,9-i,-1):
                com*=j
            dp[i]=dp[i-1]+com
        print(1.2-1.0==0.2)
        return dp[-1]
s = Solution()
print(s.countNumbersWithUniqueDigits(2))