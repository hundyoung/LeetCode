class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        dp = [True for _ in range(0,n)]
        dp[0]= False
        dp[1]= False
        for i in range(2,int(n ** 0.5) + 1):
            if dp[i]:
                for k in range(2,n):
                    if k*i<n:
                        dp[k*i]=False
                    else:
                        break
        return dp.count(True)
s= Solution()
print(s.countPrimes(10))

