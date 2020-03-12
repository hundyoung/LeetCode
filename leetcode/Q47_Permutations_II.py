from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result_dict = {}
        def back_track( nums: List[int], temp):
            if len(nums)==0:
                key = map(lambda x:str(x),temp)
                key = "".join(key)
                result_dict[key]=temp
            original_temp = list(temp)

            for i in range(len(nums)):
                temp.append(nums[i])
                back_track(nums[:i]+nums[i+1:],temp)
                temp=list(original_temp)
        back_track(nums,[])

        return [result_dict[key] for key in result_dict]


s = Solution()
print(s.permuteUnique([1,1,2]))