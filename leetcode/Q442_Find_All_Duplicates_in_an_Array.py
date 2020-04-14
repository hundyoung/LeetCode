from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            n = abs(nums[i])
            nums[n-1] = -1*nums[n-1]
            if nums[n-1]>0:
                result.append(n)
        return result
s = Solution()
print(s.findDuplicates([2,2]))