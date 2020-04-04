from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1,len(dp)):
            max_count = 1
            for j in range(i):
                if nums[j]<nums[i]:
                    max_count= max(max_count,dp[j]+1)
            dp[i]=max_count
        return max(dp)

s= Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
