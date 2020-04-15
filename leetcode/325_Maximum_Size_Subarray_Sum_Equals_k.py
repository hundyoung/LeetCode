from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # sum_list = [0]
        sum_dict = {0:[0]}
        current_sum = 0
        count = 0
        for i in range(len(nums)):
            current_sum+=nums[i]
            index_list = sum_dict.get(current_sum,[])
            index_list.append(i+1)
            sum_dict[current_sum]=index_list
            gap = current_sum-k
            if gap in sum_dict:
                for j in range(len(sum_dict[gap])):
                    count = max(count,i-sum_dict[gap][j]+1)
        return count
s = Solution()
nums, k = [-2, -1, 2, 1],1
print(s.maxSubArrayLen(nums, k))
