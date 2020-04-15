from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp=[{0:1}]
        max_count = 0
        for i in range(1,len(A)):
            n = A[i]
            gap_dict={}
            for j in range(i-1,-1,-1):
                pre_n = A[j]
                gap = n-pre_n
                pre_gap_dict = dp[j]
                if gap not in gap_dict:
                    gap_dict[gap] = pre_gap_dict.get(gap,1)+1
                else:
                    gap_dict[gap] = max(pre_gap_dict.get(gap,1)+1,gap_dict[gap])
                max_count=max(gap_dict[gap],max_count)
            dp.append(gap_dict)
        return max_count
s = Solution()
print(s.longestArithSeqLength([20,1,15,3,10,5,8]))

