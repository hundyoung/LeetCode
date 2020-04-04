from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dp_map={}
        for i in range(len(wall)):
            current_sum = 0
            for j in range(len(wall[i])-1):
                current_sum+=wall[i][j]
                dp_map[current_sum]=dp_map.get(current_sum,0)+1\


        if len(dp_map)>0:

            return len(wall)-max(dp_map.values())
        else:
            return len(wall)
s = Solution()
a = [[1,1],[2],[1,1]]

print(s.leastBricks(a))
