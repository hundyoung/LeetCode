from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = -float('inf')
        maxNumIndex = 0
        secondMax = -float('inf')
        # dp=[-float('inf') for i in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            if num>maxNum:
                secondMax = maxNum
                # dp[i] = secondMax
                maxNum = num
                maxNumIndex = i
            elif num>secondMax:
                secondMax = num

        if maxNum>=secondMax*2:
            return maxNumIndex
        else:
            return -1



s = Solution()
print(s.dominantIndex([0,0,3,2]))