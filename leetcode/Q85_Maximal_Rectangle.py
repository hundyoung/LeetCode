from typing import List
import numpy as np

import copy
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0 or len(matrix[0])== 0:
            return 0


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if j!=0:
                    if matrix[i][j]!=0:
                        matrix[i][j] = matrix[i][j-1]+1
        # dp = copy.deepcopy(matrix)
        max_size=matrix[0][0]

        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                min_height = matrix[i][j]
                for k in range(i,len(matrix)):
                    min_height = min(min_height,matrix[k][j])
                    if min_height==0:
                        break
                    size = (k-i+1)*min_height
                    max_size = max(size,max_size)
        matrix= np.array(matrix)
        # dp= np.array(dp)
        return max_size
s=Solution()
print(s.maximalRectangle([["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]))

