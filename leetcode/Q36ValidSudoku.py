from typing import List
from pandas import DataFrame


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dp = []
        # df = DataFrame(board)
        for i in range(9):
            row = []
            for j in range(9):
                row.append({})
            dp.append(row)
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                ele = row[j]
                if ele!='.':
                    if ele not in dp[i][j].keys():
                        for k in range(j+1,len(row)):
                            dp[i][k][ele]=ele
                        for k in range(i+1,len(board)):
                            dp[k][j][ele]=ele
                        for k in range(1,3-(i%3)):
                            for l in range(j-(j%3),j-(j%3)+3):
                                dp[k+i][l][ele]=ele
                    else:
                        return False
        return True



        print(dp)
        return True


solution = Solution()
print(solution.isValidSudoku([[".",".","5",".",".",".",".",".","."],[".",".",".","8",".",".",".","3","."],[".","5",".",".","2",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","9"],[".",".",".",".",".",".","4",".","."],[".",".",".",".",".",".",".",".","7"],[".","1",".",".",".",".",".",".","."],["2","4",".",".",".",".","9",".","."]]))
