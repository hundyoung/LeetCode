from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        if len(rectangles)==0:
            return 0
        else:
            # x_left,y_left,x_right,y_right = rectangles.pop(0)
            # current_size = (x_right-x_left)*(y_right-y_left)
            total_size = 0
            # size_list= []
            for x_left,y_left,x_right,y_right in rectangles:
                current_size = (x_right - x_left) * (y_right - y_left)
                # size_list.append(current_size)
                total_size+=current_size
            def intersection(x_left_a, y_left_a, x_right_a, y_right_a,x_left_b, y_left_b, x_right_b, y_right_b):
                max_x_left = max(x_left_a, x_left_b)
                max_y_left = max(y_left_a, y_left_b)
                min_x_right = min(x_right_a, x_right_b)
                min_y_right = min(y_right_a, y_right_b)
                return max_x_left,max_y_left,min_x_right,min_y_right
            for i in range(len(rectangles)):
                x_left_a, y_left_a, x_right_a, y_right_a = rectangles[i]
                x_left_inter, y_left_inter, x_right_inter, y_right_inter = rectangles[i]
                for j in range(i+1,len(rectangles)):
                    x_left_b, y_left_b, x_right_b, y_right_b = rectangles[j]
                    # if x_right_a<=x_left_b or y_right_a<=y_left_b or x_right_b<=x_left_a or y_right_b<=y_left_a:
                    #     continue
                    max_x_left,max_y_left,min_x_right,min_y_right = intersection(x_left_a, y_left_a, x_right_a, y_right_a,x_left_b, y_left_b, x_right_b, y_right_b)
                    x_left_inter, y_left_inter, x_right_inter, y_right_inter = intersection(x_left_inter, y_left_inter, x_right_inter, y_right_inter, x_left_b, y_left_b, x_right_b, y_right_b)
                    intersaction_size =(min_x_right-max_x_left)*(min_y_right-max_y_left) if (min_x_right-max_x_left)>0 and (min_y_right-max_y_left) else 0
                    # size_list[i]=size_list[i]-intersaction_size
                    total_size-=intersaction_size
                intersaction_size = (x_right_inter-x_left_inter)*(y_right_inter-y_left_inter)
                total_size+=intersaction_size
            # return sum(size_list)%(10**9+7)
            return total_size
s= Solution()
print(s.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
