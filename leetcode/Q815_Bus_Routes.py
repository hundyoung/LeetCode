from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stop_dict ={}
        if S==T:
            return 0
        for i in range(len(routes)):
            line = routes[i]
            for j in range(len(line)):
                stop = line[j]
                ajd_stop_set = stop_dict.get(stop,set())
                for k in range(len(line)):
                    ajd_stop = line[k]
                    if ajd_stop!=stop:
                        ajd_stop_set.add(ajd_stop)
                stop_dict[stop] =ajd_stop_set
        if S in stop_dict:
            to_process = [(1,S)]
            done_set = set()
            while len(to_process)>0:
                level,current_stop = to_process.pop(0)
                ajd_stop_set = stop_dict[current_stop]
                done_set.add(current_stop)
                for ajd_stop in ajd_stop_set:
                    if ajd_stop==T:
                        return level
                    else:
                        if ajd_stop not in done_set :
                            to_process.append((level+1,ajd_stop))
            return -1
        else:
            return -1
s= Solution()
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
print(s.numBusesToDestination(routes,S,T))
