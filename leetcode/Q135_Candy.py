from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        dp = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                dp[i]=dp[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                dp[i] = max(dp[i + 1] + 1,dp[i])

        return sum(dp)
s = Solution()
print(s.candy([1,0,2]))