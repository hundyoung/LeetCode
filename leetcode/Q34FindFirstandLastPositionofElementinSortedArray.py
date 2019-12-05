from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        left = self.halfSearch(nums,target-0.5,True)
        right = self.halfSearch(nums,target+0.5,False)
        if left>right:
            return [-1,-1]
        return [left,right]

    def halfSearch(self,nums: List[int], target: int,flag):
        left = 0
        right = len(nums)-1
        while left<right:
            center = (left+right)//2
            centerValue = nums[center]
            if centerValue>target:
                right =center-1
            else:
                left = center +1
        if flag:
            if nums[left]<target:
                left+=1
        else:
            if nums[left]>target:
                left-=1
        return left

solution = Solution()
print(solution.searchRange([1],1))