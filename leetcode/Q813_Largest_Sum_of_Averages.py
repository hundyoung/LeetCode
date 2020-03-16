from typing import List
import numpy as np

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        length = len(A)

        dp = [[0 for j in range(length)] for i in range(K)]
        current_sum = 0
        for i in range(length):
            current_n= A[i]
            current_sum+=current_n
            dp[0][i] = current_sum/(i+1)
        # dp = np.array(dp)
        for i in range(1,K):
            for j in range(1,length):
                if j>=i:
                    # current_n = A[j]
                    for k in range(j-1,-1,-1):
                        left_sect = dp[i-1][k]
                        right_sect = sum(A[k+1:j+1])/(j-k)
                        dp[i][j]=max(dp[i][j],(left_sect+right_sect))
        return dp[-1][-1]

s = Solution()
print(s.largestSumOfAverages([9,1,2,3,9],3))