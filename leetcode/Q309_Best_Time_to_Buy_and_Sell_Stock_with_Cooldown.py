from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        dp=[[0,0,0] for i in range(len(prices))]
        dp[0]=[0,-prices[0],float('-inf')]
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2]=dp[i-1][1]+prices[i]
        return max(dp[-1])
s = Solution()
print(s.maxProfit([1,2,3,0,2]))
