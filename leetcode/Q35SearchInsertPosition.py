from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left<right:
            middle = (left+right)>>1
            middleValue = nums[middle]
            if middleValue==target:
                return middle
            elif middleValue<target:
                left = middle+1
            else:
                right = middle
        return left

solution = Solution()
print(solution.searchInsert(   [1,3,5,6], 0))