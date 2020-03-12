from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        while i<len(nums)-1:
            current_max = nums[i]
            next_max = 0
            next_i=i
            for j in range(1,min(current_max+1,len(nums)-i)):
                next_i_candidate = j+i
                if next_max<=nums[next_i_candidate]+next_i_candidate:
                    next_max = nums[next_i_candidate]+next_i_candidate
                    next_i = next_i_candidate
            if i==next_i:
                break
            else:
                i = next_i
        return i>=len(nums)-1


s = Solution()
print(s.canJump([1,2,3]))