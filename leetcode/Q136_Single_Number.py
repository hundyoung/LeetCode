from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
        return xor
s=Solution()
print(s.singleNumber([4,1,2,1,2]))

