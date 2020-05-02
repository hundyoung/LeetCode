from typing import List


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = [[0]*len(A) for _ in range(len(A))]

        for l in range(2,len(A)):
            for i in range(len(A)):
                j=i+l
                if j>=len(A):
                    break
                dp[i][j] =float('inf')
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j]+A[i]*A[j]*A[k])

        return dp[0][-1]

s = Solution()
print(s.minScoreTriangulation([1,3,1,4,1,5]))


