from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result_list = []
        pre_length = 0
        while pre_length != len(intervals):
            pre_length = len(intervals)
            for i,j in intervals:
                change_flag = False
                k=0
                while k <len(result_list):
                    left,right= result_list[k]
                    if (i<=right and j>=left) or (i>=right and j<=left) or (i>=left and j<=right):
                        left, right = result_list.pop(k)
                        left = min(left,i)
                        right=max(right,j)
                        change_flag=True
                        result_list.append([left,right])
                        break
                    k+=1
                if not change_flag:
                    result_list.append([i, j])
            intervals = result_list
            result_list = []
        return intervals

s = Solution()
print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))