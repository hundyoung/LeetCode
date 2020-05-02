class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp=[[[0]*k for i in range(m)] for j in range(n)]
        for i in range(m):
            dp[0][i][0]=1
        for l in range(1,n):
            for i in range(m):
                for c in range(0,k):
                    bigger_count =0
                    if c>0:
                        for j in range(i+1,m):
                            bigger_count+=dp[l-1][j][c-1]%(1000000007)
                    less_count = (i+1)*dp[l-1][i][c]%(1000000007)
                    dp[l][i][c]=bigger_count%(1000000007)+less_count%(1000000007)
        result =0
        for i in range(m):
            result+=dp[n-1][i][k-1]%(1000000007)
        return result%(1000000007)
s = Solution()
n = 37
m = 17
k = 7
print(s.numOfArrays(n,m,k))