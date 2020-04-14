class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_list=[0]*300
        self.current_max =300
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp<=self.current_max:
            self.time_list[timestamp-(self.current_max-300)-1]+=1
        else:
            if timestamp-300 < self.current_max:
                new_time_list = [0] * (timestamp - self.current_max)
                new_time_list[-1] = 1
                self.time_list=self.time_list[timestamp-self.current_max:]+new_time_list
                self.current_max = timestamp
            else:
                self.time_list = [0] * 300
                self.time_list[0]=1
                self.current_max = timestamp+ 300-1


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp<=self.current_max:
            return sum(self.time_list[:timestamp-(self.current_max-300)])
        else:
            if timestamp-300 <= self.current_max:
                return sum(self.time_list[timestamp-self.current_max:])
            else:
                return 0


# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
# obj.hit(100)
# obj.hit(151)
#
# print(obj.getHits(173))
# print(obj.getHits(179))
# obj.hit(188)
# print(obj.getHits(250))
# print(obj.getHits(267))
# print(obj.getHits(396))
# print(obj.getHits(410))
# obj.hit(1)
# obj.hit(2)
# obj.hit(3)
# print(obj.getHits(4))
# obj.hit(300)
# print(obj.getHits(300))
# print(obj.getHits(301))
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))
obj.hit(300)
print(obj.getHits(300))
print(obj.getHits(301))
obj.hit(1466000001)
obj.hit(1466000002)
obj.hit(1466000003)
print(obj.getHits(1466000004))
obj.hit(1466000300)
print(obj.getHits(1466000300))
print(obj.getHits(1466000301))
