class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]* i for i in range(1,query_row+2)]
        dp[0][0] = poured
        for i in range(query_row+1):
            for j in range(len(dp[i])):
                current_n = dp[i][j]
                if current_n>1:
                    if i+1<len(dp):
                        dp[i+1][j]=dp[i+1][j]+(current_n-1)/2
                        dp[i + 1][j+1]=dp[i + 1][j+1]+(current_n-1)/2
                    dp[i][j]=1
        return dp[query_row][query_glass]
s = Solution()
print(s.champagneTower(4,0,0))
