from typing import List

import copy
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        nums.sort()
        dp = [[nums[i]]for i in range(len(nums))]
        max_len = 0
        max_len_i=0
        for i in range(1,len(nums)):
            n1 = nums[i]
            for j in range(0,i):
                n2 = nums[j]
                if n1%n2==0 and len(dp[i])<len(dp[j])+1:
                    dp[i]=copy.deepcopy(dp[j])
                    dp[i].append(n1)
            if len(dp[i])>max_len:
                max_len = len(dp[i])
                max_len_i  = i
        return dp[max_len_i]
s = Solution()
print(s.largestDivisibleSubset([3,4,16,8]))



