from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                live_cell_count = 0
                current_cell = board[i][j]
                for x,y in directions:
                    if i+x<0 or i+x>=len(board) or j+y<0 or j+y>=len(board[i+x]):
                        continue
                    side_cell = board[i+x][j+y]
                    if side_cell==1 or side_cell==2:
                        live_cell_count+=1
                if current_cell==1:
                    if live_cell_count<2:
                        board[i][j] = 2
                    elif live_cell_count>3:
                        board[i][j]=2
                else:
                    if live_cell_count==3:
                        board[i][j]=-1
        for i in range(len(board)):
            for j in range(len(board[i])):
                current_cell = board[i][j]
                if current_cell==2:
                    board[i][j]=0
                elif current_cell==-1:
                    board[i][j]=1
