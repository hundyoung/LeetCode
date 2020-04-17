from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.insert(0,1)
        nums.append(1)
        dp = [[ 0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)-2):
            dp[i][i]=0
            dp[i][i+1]=0
            dp[i][i+2]=nums[i]*nums[i+1]*nums[i+2]
        for k in range(3,len(nums)):
            for start in range(0,len(nums)-k):
                end=start+k
                for i in range(start+1,end):
                    dp[start][end]= max(dp[start][end],dp[start][i]+dp[i][end]+nums[start]*nums[end]*nums[i])

        return dp[0][-1]
s = Solution()
print(s.maxCoins([3,1,5,8]))