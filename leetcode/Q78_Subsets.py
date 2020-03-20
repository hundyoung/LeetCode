from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result_list =[]
        def back_tack(i,temp:List[int]):

            if i<len(nums):

                temp_copy = list(temp)
                temp_copy.append(nums[i])

                back_tack(i+1,temp)
                back_tack(i+1,temp_copy)
            else:
                result_list.append(temp)

        back_tack(0,[])
        return result_list

s = Solution()
print(s.subsets( [1,2,3]))

