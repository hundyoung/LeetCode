from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(matrix):
            for j in range(matrix[i]):
                node = matrix[i][j]
                if node=='1':
                    if matrix[i][j]:
                        pass
