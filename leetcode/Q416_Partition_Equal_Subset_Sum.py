from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        bag = sum(nums)/2
        if int(bag)!=bag or len(nums)<2:
            return False
        else:
            bag= int(bag)
            dp = [[False]*len(nums) for _ in range(bag+1)]
            for i in range(len(nums)):
                dp[0][i]=True
            for i in range(1,bag+1):
                for j in range(1,len(nums)):
                    if i-nums[j]>=0:
                        dp[i][j]=dp[i][j-1] or dp[i-nums[j]][j-1]
                    else:
                        dp[i][j] = dp[i][j - 1]
            return True in dp[-1]
s = Solution()
print(s.canPartition([1, 5, 11, 5]))

