from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        def calculate(nums):
            dp = [0]*len(nums)

            dp[0]=nums[0]
            if nums[0]<nums[1]:
                dp[1]= nums[1]
            else:
                dp[1] = nums[0]
            i=2
            while i <len(nums):
                n = nums[i]
                if dp[i-2]+n>dp[i-1]:
                    dp[i]=dp[i-2]+n
                else:
                    dp[i]=dp[i-1]
                i+=1
            return dp[-1]
        return max(calculate(nums[0:-1]),calculate(nums[1:]))
s = Solution()
print(s.rob([0,0]))