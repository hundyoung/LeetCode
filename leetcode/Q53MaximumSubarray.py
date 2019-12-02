from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        dp = [ 0 for i in range(len(nums))]
        dp[0] = nums[0]
        maxSum = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            currentSum = max(dp[i-1]+num,num)
            maxSum = max(currentSum,maxSum)
            dp[i] = currentSum
        return maxSum

s = Solution()
print(s.maxSubArray([1]))