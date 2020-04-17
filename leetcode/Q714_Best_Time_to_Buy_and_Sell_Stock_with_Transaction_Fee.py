from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices)==0:
            return 0
        dp = [[0,float('-inf')] for _ in range(len(prices))]
        dp[0]=[0,-prices[0]]
        for i in range(1,len(prices)):
            dp[i][0]= max(dp[i-1][0],dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]
s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], fee = 2))
