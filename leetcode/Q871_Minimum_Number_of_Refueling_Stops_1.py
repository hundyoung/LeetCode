from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel>=target:
            return 0
        if len(stations)==0:
            return -1
        dp = [0] * (len(stations)+1)
        dp[0] = startFuel
        station_flag = [True]*len(stations)
        for t in range(1,len(stations)+1):
            pre_max_dist = dp[t-1]
            max_fuel = 0
            max_fuel_i = -1
            for i in range(len(stations)):
                if station_flag[i]:
                    dist, fuel = stations[i]
                    if dist<=pre_max_dist:
                        if fuel>max_fuel:
                            max_fuel=fuel
                            max_fuel_i=i
            if max_fuel_i==-1:
                return -1
            station_flag[max_fuel_i]= False
            dp[t] = pre_max_dist+max_fuel
            if dp[t]>=target:
                return t
        return -1
s =Solution()
target = 100
startFuel = 50
stations =  [[50,50]]
print(s.minRefuelStops(target,startFuel,stations))

