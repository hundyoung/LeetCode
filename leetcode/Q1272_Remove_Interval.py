from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        i,j = toBeRemoved
        for left, right in intervals:
            if right>=i and left<i and right<j:
               result.append([left,i])
            elif left<=j and right>j and left>i:
                result.append([j,right])
            if left<i and right>=j:
                result.append([left,i])
            if left<=i and right>j:
                result.append([j,right])
            if right<=i or left>=j:
                result.append([left,right])
        return result

s = Solution()
intervals = [[0,100]]
toBeRemoved = [0,50]
print(s.removeInterval(intervals,toBeRemoved))