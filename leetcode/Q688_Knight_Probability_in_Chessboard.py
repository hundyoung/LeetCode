import copy
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp=[[0]*N for _ in range(N)]
        dp[r][c]=1
        dir=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        for k in range(1,K+1):
            pre_dp = copy.deepcopy(dp)
            for i in range(N):
                for j in range(N):
                    current_sum=0
                    for a,b in dir:
                        x,y = i+a,j+b
                        if 0<=x<N and 0<=y<N:
                            current_sum+=pre_dp[x][y]
                    dp[i][j]=current_sum/len(dir)
        result = 0
        for i in range(N):
            for j in range(N):
                result+=dp[i][j]
        return result
s =Solution()
print(s.knightProbability(3, 2, 0, 0))