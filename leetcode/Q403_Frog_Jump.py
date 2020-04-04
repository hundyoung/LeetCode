from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones)==0:
            return False
        dp_map = {}
        for i in range(len(stones)):
            dp_map[stones[i]] = set()
        dp_map[stones[0]]=set([0])
        for i in range(len(stones)):
            current_pos = stones[i]
            steps = dp_map[current_pos]
            for step in steps:
                for j in range(-1,2):
                    next_step = step+j
                    if current_pos+next_step> current_pos and current_pos+next_step in dp_map:
                        array = dp_map[current_pos+next_step]
                        array.add(next_step)
                        dp_map[current_pos + next_step] = array
        return len(dp_map[stones[-1]])>0
s = Solution()
print(s.canCross([0,1,3,6,7]))