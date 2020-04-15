from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1,int(sqrt(n))+1)]
        dp = [n]*(n+1)
        dp[0] =0
        for i in range(1,n+1):
            for sn in square_nums:
                if sn>i:
                    break
                dp[i] = min(dp[i],dp[i-sn]+1)
        return dp[-1]
s =Solution()
print(s.numSquares(13))


