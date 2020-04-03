from typing import List

import itertools
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_diff = float('inf')
        # if "00:00" in timePoints:
        #     timePoints.append("24:00")
        for i,j in itertools.combinations(timePoints,2):
            i_strs = i.split(":")
            i_hour = i_strs[0]
            i_mins = int(i_strs[1])+60*int(i_hour)
            j_strs = j.split(":")
            j_hour = j_strs[0]
            j_mins = int(j_strs[1])+60*int(j_hour)
            min_diff = min(max(i_mins,j_mins)-min(i_mins,j_mins),min_diff,(24*60)-max(i_mins,j_mins)+min(i_mins,j_mins))
        return min_diff
s =Solution()
print(s.findMinDifference(["23:59","00:00"]))

