from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        nums.sort()
        pre_n=nums[0]
        result = [pre_n]
        for i in range(1,len(nums)):
            n = nums[i]
            if n>=pre_n**2:
                result.append(n)
                pre_n=n
        print(2//10000001)
        return result
s = Solution()
print(s.largestDivisibleSubset([2,10000,10000001]))



