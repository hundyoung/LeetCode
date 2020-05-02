from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        else:
            # dp=[[0,0] for i in range(len(nums))]
            # dp[0]=[0,0]
            # dp[1]=[1,1]
            # for i in range(2,len(nums)):
            #     dp[i][0]=dp[i-1][0]
            if nums[1]>nums[0]:
                is_up=-1
            elif nums[1]<nums[0]:
                is_up=1
            else:
                is_up=0
            pre_n = nums[1]
            count=2
            for i in range(2,len(nums)):
                n = nums[i]
                if n>pre_n and is_up==1:
                    count+=1
                    pre_n=n
                    is_up= -1
                elif n<pre_n and is_up==-1:
                    count+=1
                    pre_n=n
                    is_up=1
            return count
s = Solution()
print(s.wiggleMaxLength([0,0]))

