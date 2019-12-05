from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]

        maxMoney = 0
        if len(dp)>0:
            dp[0] = nums[0]
            maxMoney = nums[0]
            if len(dp)>1:
                dp[1] = nums[1]

                maxMoney = max(nums[1],maxMoney)
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2],dp[i-3])+nums[i]
            maxMoney = max(dp[i],maxMoney)
        return maxMoney


s = Solution()
print(s.rob([2,1,1,2]))