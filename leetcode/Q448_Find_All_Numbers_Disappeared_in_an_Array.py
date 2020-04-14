from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            n = abs(nums[i])
            nums[n-1]=-abs(nums[n-1])
        result = []
        for i in range(len(nums)):
            n = nums[i]
            if n>0:
                result.append(i+1)
        return result
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
