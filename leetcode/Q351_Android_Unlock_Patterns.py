import copy
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.result=0
        points=[]
        for i in range(3):
            for j in range(3):
                points.append((i,j))
        def back_track(grid,i,j,count:int,isMid):
            if count>=m:
                if isMid:
                    self.result+=1
                else:
                    self.result+=4
            if count>n-1:
                return
            for k in range(len(points)):
                next_i,next_j = points[k]
                if not grid[next_i][next_j] :
                    continue
                if (i==next_i or j==next_j) and ((next_i-i)**2==4 or (next_j-j)**2==4) and grid[(i+next_i)//2][(j+next_j)//2]:
                    continue
                if ((next_i-i)**2==4 and (next_j-j)**2==4) and grid[(i+next_i)//2][(j+next_j)//2]:
                    continue
                grid_copy = copy.deepcopy(grid)
                grid_copy[next_i][next_j]=False
                back_track(grid_copy,next_i,next_j,count+1,isMid)
        # grid=[[True]*3]*3
        grid = [[True] * 3 for _ in range(3)]
        grid[0][0]=False
        back_track(grid,0,0,1,False)
        grid = [[True] * 3 for _ in range(3)]
        grid[0][1]=False
        back_track(grid,0,1,1,False)
        grid = [[True] * 3 for _ in range(3)]
        grid[1][1]=False
        back_track(grid,1,1,1,True)
        return self.result


s = Solution()
print(s.numberOfPatterns(1,3))

