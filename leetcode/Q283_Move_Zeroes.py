from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        zero_count =0
        while i <len(nums)-zero_count:
            n = nums[i]
            if n ==0:
                j = i
                while j<len(nums)-1:
                    temp = nums[j+1]
                    nums[j+1]= nums[j]
                    nums[j] = temp
                    j+=1
                zero_count+=1
            else:
                i+=1

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))