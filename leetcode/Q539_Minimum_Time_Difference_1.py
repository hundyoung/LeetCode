from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_point_list = []
        for i in range(len(timePoints)):
            i_strs = timePoints[i].split(":")
            i_hour = i_strs[0]
            i_mins = int(i_strs[1]) + 60 * int(i_hour)
            time_point_list.append(i_mins)
        time_point_list.sort()
        min_diff = (24*60)-time_point_list[-1]+time_point_list[0]
        for i in range(len(time_point_list)-1):
            min_diff=min(time_point_list[i+1]-time_point_list[i],min_diff)
        return min_diff
s =Solution()
print(s.findMinDifference(["23:59","00:00"]))

