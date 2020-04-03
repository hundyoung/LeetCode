from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # dp = [[0]*4 for i in range(len(A))]
        def maxSum(A,L,M):
            pre_sum = [0]
            current_sum = 0
            for i in range(len(A)):
                current_sum = current_sum+A[i]
                pre_sum.append(current_sum)
            dp_L = [0]*(len(A)-1)
            dp_M = [0]*(len(A)-1)
            for i in range(L,len(A)-M+1):
                current_sum_L = pre_sum[i]-pre_sum[i-L]
                dp_L[i-1] = max(current_sum_L,dp_L[i-2])
            for i in range(len(A)-M,L-1,-1):
                current_sum_M = pre_sum[i+M]-pre_sum[i]
                dp_M[i-1] =  max(current_sum_M,dp_M[i-2])
            max_sum = 0
            for i in range(len(dp_M)):
                max_sum=max(max_sum,dp_M[i]+dp_L[i])
            return max_sum
        return max(maxSum(A,L,M),maxSum(A,M,L))

s =Solution()
A = [2,1,5,6,0,9,5,0,3,8]
L =4
M = 3
print(s.maxSumTwoNoOverlap(A,L,M))
