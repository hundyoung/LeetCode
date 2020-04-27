from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums) == 1:
            return 1
        dp=[[1,1] for i in range(len(nums))]
        if nums[1]>nums[0]:
            dp[1]=[2,1]
        elif nums[1]<nums[0]:
            dp[1]=[1,2]
        else:
            dp[1]=[1,1]
        for i in range(2,len(nums)):
            n = nums[i]
            if n>nums[i-1]:
                dp[i][0]=dp[i-1][1]+1
                dp[i][1]=dp[i-1][1]
            elif n<nums[i-1]:
                dp[i][0]=dp[i-1][0]
                dp[i][1]=dp[i-1][0]+1
            else:
                dp[i][0]=dp[i-1][0]
                dp[i][1]=dp[i-1][1]
        return max(dp[-1])

s = Solution()
print(s.wiggleMaxLength([126,37,130,225,239,77,235,333,30,69,294,128,163,17,224,229,128,59,205,265,328,259,337,93,354,316,309,67,36,88,133,359,8,335,247,209,279,94,41,62]))

