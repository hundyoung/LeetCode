from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        if len(rectangles)==0:
            return 0
        else:
            event = []
            for x1,y1,x2,y2 in rectangles:
                event.append((y1,True,x1,x2))
                event.append((y2,False,x1,x2))
            event = sorted(event,key=lambda x:x[0])

            pre_y,flag,x1,x2 = event.pop(0)
            active_list = [(x1,x2)]
            area = 0
            def caculate_current_area():
                current_area = 0
                index = -1
                for x1,x2 in active_list:
                    index = max(x1,index)
                    current_area+=max(0,x2-index)
                    index=max(x2,index)
                return current_area
            for y,flag,x1,x2 in event:
                area+=(caculate_current_area()*(y-pre_y))
                if flag:
                    active_list.append((x1,x2))
                    active_list.sort()
                else:
                    active_list.remove((x1,x2))
                pre_y = y

            return area%(10 ** 9 + 7 )


s= Solution()
print(s.rectangleArea([[49,40,62,100],[11,83,31,99],[19,39,30,99]]))
