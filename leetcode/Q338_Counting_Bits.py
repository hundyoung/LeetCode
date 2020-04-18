from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num==0:
            return [0]
        dp = [0]*(num+1)
        dp[0]=0
        dp[1]=1
        for i in range(num+1):
            dp[i]=dp[i>>1]+i%2
        return dp
s = Solution()
print(s.countBits(1))

