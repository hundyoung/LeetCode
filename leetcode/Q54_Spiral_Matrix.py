from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # direction = 'right'
        result = []
        if len(matrix)==0:
            return result
        def back_track(init_direction,direction:str,x,y):
            if init_direction==direction:
                return
            if direction=='right':
                j=y
                while j<len(matrix[x]):
                    if matrix[x][j]!='.':
                        result.append(matrix[x][j])
                        matrix[x][j]='.'
                        init_direction='right'
                    else:
                        break
                    j+=1
                back_track(init_direction,'down',x+1,j-1)
            elif direction=='down':
                i = x
                while i <len(matrix):
                    if matrix[i][y]!='.':
                        result.append( matrix[i][y])
                        matrix[i][y]='.'
                        init_direction='down'
                    else:
                        break
                    i+=1
                back_track(init_direction,'left',i-1,y-1)
            elif direction == 'left':
                j = y
                while j >=0:
                    if matrix[x][j] != '.':
                        result.append(matrix[x][j])
                        matrix[x][j]='.'
                        init_direction='left'
                    else:
                        break
                    j -= 1
                back_track(init_direction,'up', x-1, j + 1)
            elif direction=='up':
                i = x
                while i >=0:
                    if matrix[i][y]!='.':
                        result.append( matrix[i][y])
                        matrix[i][y]='.'
                        init_direction='up'
                    else:
                        break
                    i-=1
                back_track(init_direction,'right',i+1,y+1)

        back_track('up','right',0,0)
        return result

s = Solution()
x = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(s.spiralOrder(x))