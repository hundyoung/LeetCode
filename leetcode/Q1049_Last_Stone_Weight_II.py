from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum=sum(stones)
        bag_size=(stones_sum+1)//2
        dp=[[0]*len(stones) for _ in range(bag_size+1)]
        for i in range(1,bag_size+1):
            if i>=stones[0]:
                dp[i][0]=stones[0]
        for j in range(0,len(stones)):
            if stones[j]==1:
                dp[1][j]=1
        for i in range(1,bag_size+1):
            for j in range(1,len(stones)):
                if i>=stones[j]:
                    dp[i][j]=max(dp[i-stones[j]][j-1]+stones[j],dp[i][j-1])
                else:
                    dp[i][j]=dp[i][j-1]
        return abs(stones_sum-2*dp[-1][-1])
s = Solution()
print(s.lastStoneWeightII([57,32,40,27,35,61]))

