from typing import List
import numpy as np

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_size = 0
        matrix =list(map(lambda x:list(map(lambda a:int(a),x)),matrix))
        matrix = np.array(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                node = matrix[i][j]
                if node==1:
                    if i - 1 >= 0 and j - 1 >= 0:
                        left_up = matrix[i-1][j-1]
                        square_flag =True
                        for k in range(1,left_up+1):
                            if matrix[i-k][j] == 0 or matrix[i][j-k] == 0:
                                square_flag=False
                                break
                            else:
                                matrix[i][j] = k+1
                        if square_flag:
                            matrix[i][j] = matrix[i - 1][j - 1] + 1
                    max_size = max(max_size,matrix[i][j])
        return max_size**2
s = Solution()
print(s.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]))
