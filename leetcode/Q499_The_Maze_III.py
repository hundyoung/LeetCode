from typing import List
import numpy as np

import copy
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        maze=np.asarray(maze)

        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        dirs = ['u','r','d','l']
        steps=0
        to_process=[[steps,[tuple(ball)],'']]
        results = []
        min_steps = float('inf')
        while len(to_process)>0:
            steps,path,dir = to_process.pop(0)
            x,y = path[-1]
            for i in range(len(directions)):
                r, c=directions[i]
                next_x=x
                next_y=y
                current_step = 0
                while r!=0 and next_x+r>=0 and next_x+r<len(maze) and maze[next_x+r][next_y]!=1 and (next_x,next_y)!=tuple(hole):
                    next_x=next_x+r
                    current_step+=1
                    if (next_x,next_y)==ball or (next_x,next_y) in path:
                        break
                while c!=0 and next_y+c>=0 and next_y+c<len(maze[0]) and maze[next_x][next_y+c]!=1 and (next_x,next_y)!=tuple(hole):
                    next_y = next_y+c
                    current_step+=1
                    if (next_x,next_y)==ball or (next_x,next_y) in path:
                        break
                if (next_x,next_y)!=(x,y) and (next_x,next_y) not in path and maze[next_x][next_y]!=1:
                    new_path = copy.deepcopy(path)
                    new_path.append((next_x, next_y))
                    if next_x==hole[0] and next_y == hole[1]:
                        min_steps=min(min_steps,steps+current_step)
                        results.append((steps+current_step,dir+dirs[i]))
                        # min_steps=steps+current_step
                    else:
                        if steps+current_step <= min_steps:
                            to_process.append([steps+current_step,new_path,dir+dirs[i]])
        if len(results)==0:
            return 'impossible'
        results= sorted(results,key=lambda x:(x[0],x[1]))
        return results[0][1]




s = Solution()
maze,ball,hole=[[0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0],[1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0],[0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1]],[27,5],[2,3]
print(s.findShortestWay(maze,ball,hole))