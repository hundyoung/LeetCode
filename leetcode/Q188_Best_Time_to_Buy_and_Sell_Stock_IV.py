from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfit( prices: List[int]) -> int:
            if len(prices) == 0:
                return 0
            dp = [[0, 0] for i in range(len(prices))]
            dp[0] = [0, -prices[0]]
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            return dp[-1][0]
        if len(prices)==0 or k==0:
            return 0
        if k>len(prices)//2:
            return maxProfit(prices)
        dp=[[[0,float('-inf')] for k in range(k+1)] for i in range(len(prices))]

        for i in range(0,len(prices)):
            dp[i][1] = [0, -prices[i]]

        # dp[0][2]=[float('-inf'),float('-inf')]
        # dp[0][1]=[float('-inf'),-prices[0]]
        # dp[0][0]=[0,float('-inf')]
        max_profit = 0
        for i in range(1,len(prices)):
            for j in range(1,k+1):
                if i>=j:
                    dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
                    dp[i][j][1]=max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i])
                    max_profit = max(max_profit,dp[i][j][0],dp[i][j][1])
        return max_profit
s = Solution()
print(s.maxProfit(5, [5,5,4,9,3,8,5,5,1,6,8,3,4]))
