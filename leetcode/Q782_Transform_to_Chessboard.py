from typing import List

import math
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        row_dict={}
        for i in range(len(board)):
            row = board[i]
            one_count = row.count(1)
            zero_count = len(row)-one_count
            if not 0<=max(zero_count,one_count)-min(zero_count,one_count)<=1:
                return -1
            row = list(map(lambda x:str(x),row))
            row = ''.join(row)
            row_dict[row] = row_dict.get(row,0)+1
        if len(row_dict)!=2:
            return -1
        row_candidate={}
        start=0
        for i in range(2):
            candidate = []
            one_count=0
            for j in range(len(board[0])):
                start = 1-start
                candidate.append(str(start))
                if start==1:
                    one_count+=1
            row_candidate[''.join(candidate)]=one_count

        row_diff_count = float('inf')
        for row in row_dict:
            for key in row_candidate:
                count =0
                one_count=row_candidate[key]
                if one_count==row.count('1'):
                    for j in range(len(row)):
                        if row[j]!=key[j]:
                            count+=1
                    row_diff_count = min(row_diff_count,count)

        column_dict ={}
        for j in range(len(board[0])):
            column = ''
            one_count=0
            for i in range(len(board)):
                column+=str(board[i][j])
                if board[i][j]==1:
                    one_count+=1
            zero_count = len(column)-one_count
            if not 0<=max(zero_count,one_count)-min(zero_count,one_count)<=1:
                return -1
            column_dict[column] = column_dict.get(column,0)+1
        if len(column_dict)!=2:
            return -1

        column_candidate = {}
        for i in range(2):
            candidate = []
            one_count=0
            for j in range(len(board)):
                start = 1-start
                candidate.append(str(start))
                if start==1:
                    one_count+=1
            column_candidate[''.join(candidate)]=one_count

        column_diff_count = float('inf')
        for column in column_dict:
            for key in column_candidate:
                count =0
                one_count=row_candidate[key]
                if one_count==column.count('1'):
                    for j in range(len(column)):
                        if column[j]!=key[j]:
                            count+=1
                    column_diff_count = min(column_diff_count,count)
        return math.ceil(column_diff_count/2)+math.ceil(row_diff_count/2)
s = Solution()
board = [[1,0,0,1,1],[0,1,1,0,0],[1,0,0,1,1],[0,1,1,0,0],[0,1,1,0,0]]
print(s.movesToChessboard(board))



