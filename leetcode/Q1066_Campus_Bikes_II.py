from typing import List

import copy
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        if len(workers)==0:
            return 0
        dist_map=[[0]*len(bikes) for _ in range(len(workers))]
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist_map[i][j]=abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
        self.dp={}
        def back_track(i:int,used_bikes:set):
            if i == len(workers):
                return 0
            state = (i, tuple(sorted(list(used_bikes))))
            if state in self.dp:
                return self.dp[state]
            else:
                min_dist = float('inf')
                for j in range(len(bikes)):
                    if j not in used_bikes:
                        current_dist = dist_map[i][j]
                        used_bikes_copy = copy.deepcopy(used_bikes)
                        used_bikes_copy.add(j)
                        dist=current_dist+back_track(i+1,used_bikes_copy)
                        min_dist = min(min_dist, dist)
                self.dp[state]=min_dist
                return min_dist
        a = back_track(0,set())
        return a

s = Solution()
print(s.assignBikes([[0,0],[1,1],[2,0]],[[1,0],[2,2],[2,1]]))