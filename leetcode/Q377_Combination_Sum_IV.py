from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            current_total = 0
            for j in range(len(nums)):
                n = nums[j]
                if i-n>=0:
                    current_total+=dp[i-n]
            dp[i]=current_total
        return dp[target]

s = Solution()
print(s.combinationSum4([1, 2, 3],4))