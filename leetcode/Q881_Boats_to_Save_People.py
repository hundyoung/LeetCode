from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people)==0:
            return 0
        people = sorted(people,reverse=True)
        people_flag = [True]*len(people)
        count = 0
        while people_flag.count(True)>0:
            left=limit
            i=0
            seat_count =0
            while i <len(people) and seat_count<2:
                if people_flag[i] and left>=people[i]:
                    left-=people[i]
                    people_flag[i]=False
                    seat_count+=1
                else:
                    i+=1
            count+=1
        return count

s = Solution()
people = [3,2,3,2,2]
limit = 6
print(s.numRescueBoats(people,limit))

