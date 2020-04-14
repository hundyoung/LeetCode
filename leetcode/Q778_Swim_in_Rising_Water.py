from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        done = set()
        start = (0, 0)
        end = (len(grid) - 1, len(grid[0]) - 1)
        done.add(start)
        level = grid[0][0]
        found_end= False
        while end not in done:
            current_min = float('inf')
            current_min_x = -1
            current_min_y = -1
            for x, y in done:
                for i, j in directions:
                    if x + i < len(grid) and x + i >= 0 and y + j < len(
                            grid[0]) and y + j >= 0:
                        if (x + i,y + j)==end:
                            found_end=True
                            current_min = grid[x + i][y + j]
                            current_min_x = x + i
                            current_min_y = y + j
                            break
                        elif (x + i,y + j) not in done and grid[x + i][y + j] < current_min:
                            current_min = grid[x + i][y + j]
                            current_min_x = x + i
                            current_min_y = y + j
                if found_end:
                    break
            done.add((current_min_x, current_min_y))
            level = max(current_min, level)
        return level


s = Solution()
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(s.swimInWater(grid))
