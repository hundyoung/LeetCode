from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new = [False for i in range(len(nums)+2)]
        for i in range(len(nums)):
            ele = nums[i]
            if ele>0 and ele<len(new):
                new[ele] = True
        for i in range(1,len(new)):
            if new[i]==False:
                return i
        return 1

s = Solution()
print(s.firstMissingPositive([1]))


#
# s = Solution()
# print(s.firstMissingPositive([3,4,-1,1]))