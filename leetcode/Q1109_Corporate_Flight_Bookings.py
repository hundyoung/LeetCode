from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # flight ={}
        flight_list = [0 for _ in range(n)]
        for flight_from, flight_to, num in bookings:
            flight_list[flight_from-1] +=num
            if flight_to<n:
                flight_list[flight_to] -=num
        for i in range(1,len(flight_list)):
            flight_list[i] +=flight_list[i-1]


        return flight_list
s= Solution()

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n =5
print(s.corpFlightBookings(bookings,n))