from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
        bitFlag = (xor & (~ (xor - 1)))
        n1=0
        n2=0
        for i in range(len(nums)):
            if nums[i]&bitFlag==0:
                n1=nums[i]^n1
            else:
                n2=nums[i]^n2
        return [n1,n2]
s=Solution()
print(s.singleNumbers([1,2,5,2]))
