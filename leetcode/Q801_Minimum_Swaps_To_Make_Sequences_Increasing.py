from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        dp=[0,1]
        for i in range(1,len(A)):
            a1,a2 = A[i-1],A[i]
            b1,b2 = B[i-1],B[i]
            if a1>=a2 or b1>=b2:
                dp[0],dp[1]=dp[1],dp[0]+1
            elif a1>=b2 or b1>=a2:
                dp[0]=dp[0]
                dp[1]=dp[1]+1
            else:
                min_dp=min(dp)
                dp[0],dp[1]=min_dp,min_dp+1
        return min(dp)
s =Solution()
A,B=[1,3,5,4],[1,2,3,7]

print(s.minSwap(A,B))

