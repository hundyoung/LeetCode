from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        K=2
        if len(prices)==0:
            return 0
        dp=[[[0,0] for k in range(K+1)] for i in range(len(prices))]

        for i in range(1,len(prices)):
            for k in range(0,K+1):
                if k ==0:
                    dp[i][k] = [0, float('-inf')]
                if k==1:
                    dp[i][k] = [0, -prices[i]]
                if k==2:
                    dp[i][k] = [0, float('-inf')]

        dp[0][2]=[float('-inf'),float('-inf')]
        dp[0][1]=[float('-inf'),-prices[0]]
        dp[0][0]=[0,float('-inf')]
        for i in range(1,len(prices)):
            for k in range(1,K+1):
                if i>=k:
                    dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
                    dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        return max(dp[-1][0][0],dp[-1][1][0],dp[-1][2][0])
s = Solution()
print(s.maxProfit([1] ))