from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # start = 0
        if len(nums)==0:
            return 0
        current_sum = float("-inf")
        max_sum = float("-inf")
        for i in range(len(nums)):
            num = nums[i]
            current_sum=max(current_sum+num,num)
            max_sum = max(current_sum,max_sum)
        return max_sum
s =Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))