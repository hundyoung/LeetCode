from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix = matrix[::-1]
        for j in range(len(matrix)):
            # first_row = matrix[0]
            for i in range(len(matrix)-1,0+j,-1):
                temp_row = matrix[i-1]
                matrix[i-1] = matrix[i]
                matrix[i] = temp_row
            # matrix[-1]=first_row
        # print(matrix)

        for i in range(len(matrix)):
            for j in range(i+1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp



        # print(matrix)
        # return matrix



s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(s.rotate(matrix))