from typing import List

import numpy as np

import copy
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        horizontal, vertical, diagonal, antidiagonal = copy.deepcopy(M),copy.deepcopy(M),copy.deepcopy(M),copy.deepcopy(M)
        max_count = 0
        # horizontal, vertical, diagonal, antidiagonal = np.asarray(horizontal),np.asarray(vertical),np.asarray(diagonal),np.asarray(antidiagonal)
        # M = np.asarray(M)
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j]==1:
                    horizontal[i][j] = horizontal[i][j-1]+1 if j-1>=0 else 1
                    vertical[i][j] = vertical[i-1][j]+1 if i-1 >=0 else 1
                    diagonal[i][j] = diagonal[i-1][j-1]+1 if i-1>=0 and j-1>=0 else 1
                    antidiagonal[i][j] = antidiagonal[i-1][j+1]+1 if i-1>=0 and j+1<len(M[i]) else 1
                    max_count = max(max_count,horizontal[i][j],vertical[i][j],diagonal[i][j],antidiagonal[i][j])
        return max_count
s =Solution()
print(s.longestLine([[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]))
