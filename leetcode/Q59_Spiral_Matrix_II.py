from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        matrix = [[False]*n for i in range(n)]
        # print(matrix)
        cx,cy = (0,0)
        d_i=0
        turn_count = 0
        i=1
        while i <n*n+1:
            dx,dy = direction[d_i%4]
            if turn_count==4:
                break
            if (cx<n and cx>=0) and (cy<n and cy>=0) and not matrix[cx][cy] :
                matrix[cx][cy]=i
                cx, cy = cx + dx, cy + dy
                i+=1
                turn_count=0
            else:
                cx, cy = cx - dx, cy - dy
                d_i += 1
                dx, dy = direction[d_i % 4]
                cx, cy = cx + dx, cy + dy
                turn_count+=1
        return matrix


s = Solution()
print(s.generateMatrix(3))