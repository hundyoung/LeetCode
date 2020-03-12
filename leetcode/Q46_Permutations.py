from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result_list = []

        def back_track( nums: List[int], temp):
            if len(nums)==0:
                result_list.append(temp)
            original_temp = list(temp)

            for i in range(len(nums)):
                temp.append(nums[i])
                back_track(nums[:i]+nums[i+1:],temp)
                temp=list(original_temp)
        back_track(nums,[])
        return result_list


s = Solution()
print(s.permute([1,2,3]))