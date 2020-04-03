from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people)==0:
            return 0
        people = sorted(people,reverse=True)
        left = 0
        right = len(people)-1
        count = 0
        while left<=right:
            count+=1
            if people[left]+people[right]<=limit:
                right-=1
            left+=1
        return count

s = Solution()
people = [3,2,3,2,2]
limit = 6
print(s.numRescueBoats(people,limit))

