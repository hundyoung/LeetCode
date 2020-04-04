from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n_dict = {}
        for i in range(len(nums)):
            n = nums[i]
            array = n_dict.get(n,[])
            if len(array)>0:
                array[0] = array[0]+1
                array[2] = i
            else:
                array.append(1)
                array.append(i)
                array.append(i)
            n_dict[n] = array
        max_degree = 0
        min_end_start = float('inf')
        for n in n_dict:
            degree,start,end = n_dict[n]
            if degree>max_degree:
                max_degree=degree
                min_end_start = end-start
            elif degree== max_degree  and end-start<min_end_start:
                max_degree=degree
                min_end_start = end-start
        return min_end_start+1
s =Solution()
print(s.findShortestSubArray( [1, 2, 2, 3, 1]))

