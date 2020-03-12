from typing import List

import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result_list = []
        matrix = [['?' for j in range(n)] for i in range(n)]

        def markDot(x, y, matrix: List[List[str]]):
            for i in range(len(matrix)):
                if matrix[i][y] == '?':
                    matrix[i][y] = '.'
                for j in range(len(matrix[0])):
                    if matrix[x][j] == '?':
                        matrix[x][j] = '.'
                    if matrix[i][j]=='?':
                        if x + y == i + j :
                            matrix[i][j] = '.'
                        if x - y == i - j :
                            matrix[i][j] = '.'
            return matrix

        def back_track(i: int, matrix: List[List[str]]):
            if i == n:
                matrix = list(map(lambda x:''.join(x),matrix))
                result_list.append(matrix)
                return
            for j in range(n):
                original_matrix = copy.deepcopy(matrix)
                if matrix[i][j]=='?':
                    matrix[i][j]='Q'
                    matrix = markDot(i,j,matrix)
                    back_track(i + 1, matrix)
                matrix=original_matrix

        back_track(0, matrix)
        return result_list


s = Solution()
print(s.solveNQueens(4))
