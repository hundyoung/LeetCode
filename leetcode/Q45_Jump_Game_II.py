from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp = [len(nums) for i in range(len(nums))]
        # max_step = nums[0]
        # dp[0]=0
        # for i in range(1,max_step+1):
        #     if i < len(nums):
        #         dp[i]=1
        # for i in range(1,len(nums)):
        i=0
        count = 0
        while i <len(nums):
            max_step = nums[i]
            next_max_step = 0
            next_max_j = 0
            if i >= len(nums) - 1:
                return count
            count+=1
            for j in range(1,max_step+1):
                next_i = j+i
                # if next_i>=len(nums)-1:
                #     return count
                next_step = j+nums[next_i]
                # if next_step>=len()
                if next_step<len(nums) and next_step>=next_max_step:
                    next_max_step = next_step
                    next_max_j = next_max_step+i
            count+=1

            i = next_max_j
        return count
s = Solution()
print(s.jump([1,2,3]))