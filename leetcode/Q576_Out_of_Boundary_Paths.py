import copy
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if N==0:
            return 0
        dp=[[0]*n for _ in range(m)]
        dp[i][j]=1
        dir=[(-1,0),(0,1),(1,0),(0,-1)]
        result=0
        for t in range(1,N):
            result+=sum(dp[0])
            result+=sum((dp[-1]))
            for k in range(m):
                result+=dp[k][0]
                result+=dp[k][-1]
            temp_dp = copy.deepcopy(dp)
            for x in range(m):
                for y in range(n):
                    current_sum = 0
                    for a,b in dir:
                        if 0<=x+a<m and 0<=y+b<n:
                            current_sum+=temp_dp[x+a][y+b]
                    dp[x][y]=current_sum

        result += sum(dp[0])
        result += sum((dp[-1]))
        for k in range(m):
            result += dp[k][0]
            result += dp[k][-1]
        return result%(10**9+ 7)
s=Solution()
# print(s.findPaths(3,8,0,2,0))
print(s.findPaths(m = 1, n = 3, N = 3, i = 0, j = 1))
