from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        line_dict ={}
        if S==T:
            return 0
        start_set = set()
        end_set=set()
        for i in range(len(routes)):
            line = routes[i]
            for j in range(i+1,len(routes)):
                another_line = routes[j]
                com = line+another_line
                if len(set(com))!=len(com):
                    line_set = line_dict.get(i,set())
                    line_set.add(j)
                    line_dict[i]=line_set
                    line_set = line_dict.get(j,set())
                    line_set.add(i)
                    line_dict[j]=line_set
            if S in line:
                start_set.add(i)
            if T in line:
                end_set.add(i)
        if len(list(start_set)+list(end_set))!=len(set(list(start_set)+list(end_set))):
            return 1
        to_process = list(map(lambda x:(1,x),start_set))
        done_set =set()
        while len(to_process)>0:
            level,line = to_process.pop(0)
            if line in line_dict:
                adj_line_set = line_dict[line]
                for another_line in adj_line_set:
                    if another_line not in done_set:
                        if another_line in end_set:
                            return level+1
                        to_process.append((level+1,another_line))
                        done_set.add(another_line)

        return -1

s= Solution()
routes = [[1],[15,16,18],[10],[3,4,12,14]]
S = 3
T = 15
print(s.numBusesToDestination(routes,S,T))
