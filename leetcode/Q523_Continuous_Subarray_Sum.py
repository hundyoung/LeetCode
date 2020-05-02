from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:
            return False
        if k==0:
            if 0 in nums and nums.index(0)+1<len(nums) and nums[nums.index(0)+1]==0:
                return True
            else:
                return False
        sum_list = [0]
        current_sum=0
        for i in range(len(nums)):
            current_sum+=nums[i]
            sum_list.append(current_sum)
        for i in range(0,len(sum_list)):
            for j in range(i+2,len(sum_list)):
                if (sum_list[j]-sum_list[i])%k==0:
                    return True
        return False
s = Solution()
print(s.checkSubarraySum([1,0], k = 2))