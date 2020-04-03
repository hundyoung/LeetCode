from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count_one = data.count(1)
        if count_one<=1:
            return 0
        current_count = data[:count_one].count(1)
        max_count = current_count
        for i in range(count_one,len(data)):
            if data[i]==1:
                current_count+=1
            if data[i-count_one]==1:
                current_count-=1
            max_count = max(max_count,current_count)
        return count_one-max_count
s = Solution()
print(s.minSwaps([1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0]))
