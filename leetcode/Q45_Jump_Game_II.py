from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        count =0
        i=0
        while i <len(nums)-1:
            n = nums[i]
            max_step =0
            next_i=i
            for step in range(1,n+1):
                j = i+step
                if j>=len(nums)-1:
                    next_i = j
                    break
                if nums[j]+j>max_step:
                    max_step=nums[j]+j
                    next_i=j
            count+=1
            i=next_i
        return count
s = Solution()
print(s.jump([2,3,1,1,4]))