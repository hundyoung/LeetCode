from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = []
        points.append(p1)
        points.append(p2)
        points.append(p3)
        points.append(p4)
        points = sorted(points,key=lambda x:(x[0],x[1]))
        def distantce(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
        l01 = distantce(points[0],points[1])
        l13 = distantce(points[1],points[3])
        l32 = distantce(points[2],points[3])
        l02 = distantce(points[0],points[2])
        l03 = distantce(points[0],points[3])
        l12 = distantce(points[1],points[2])
        return (l01==l13==l32==l02!=0)and(l03==l12)
s=Solution()
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
print(s.validSquare(p1,p2,p3,p4))
