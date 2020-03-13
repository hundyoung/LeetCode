from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # left_fuel = startFuel
        # current_location = 0
        # count=0
        if startFuel>=target:
            return 0
        c_t_i=0
        c_t_max = 0
        pre_t_max = startFuel
        for t in range(1,len(stations)+1):
            i=0
            while i <len(stations):
                location, fuel = stations[i]
                if location<=pre_t_max:
                    if fuel>c_t_max:
                        c_t_max=fuel
                        c_t_i=i
                i+=1
            stations.pop(c_t_i)
            pre_t_max=pre_t_max+c_t_max
            c_t_max=0
            if pre_t_max>=target:
                return t
        return -1

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

# target = 100
# startFuel = 50
# stations = [[25,50],[50,25]]
s = Solution()
print(s.minRefuelStops(target,startFuel,stations))