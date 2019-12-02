from typing import List

from pandas import DataFrame

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dp = []
        # df = DataFrame(board)
        for i in range(9):
            row = []
            for j in range(9):
                digDic = {}
                for i in range(0,10):
                    digDic[i]=i
                row.append(digDic)
            dp.append(row)
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                ele = row[j]
                if ele!='.':
                    ele = int(ele)
                    for k in range(0,len(row)):
                        if ele in dp[i][k].keys():
                            del dp[i][k][ele]
                    for k in range(0,len(board)):
                        if ele in dp[k][j].keys():
                            del dp[k][j][ele]
                    for k in range(i-(i%3),i-(i%3)+3):
                        for l in range(j-(j%3),j-(j%3)+3):
                            if ele in dp[k][l].keys():
                                del dp[k][l][ele]
        df = DataFrame(dp)

        return True


dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

# dict.pop('a')  # 删除键 'Name'
# print(dict)
solution = Solution()
print(solution.solveSudoku([[".",".","5",".",".",".",".",".","."],[".",".",".","8",".",".",".","3","."],[".","5",".",".","2",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","9"],[".",".",".",".",".",".","4",".","."],[".",".",".",".",".",".",".",".","7"],[".","1",".",".",".",".",".",".","."],["2","4",".",".",".",".","9",".","."]]))
