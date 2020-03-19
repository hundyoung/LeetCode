from typing import List
import copy

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result_list = []

        def back_track(i, temp_list: List[List[int]]):
            if i == len(s):
                if len(temp_list)==4:
                    result_list.append(temp_list)
            else:
                if ((len(s) - i) % 3)-2 <= (4 - len(temp_list)) and len(temp_list) <= 4:

                    temp_list_copy = copy.deepcopy(temp_list)
                    temp_list_copy.append([int(s[i])])
                    back_track(i + 1, temp_list_copy)
                    temp_list_copy = copy.deepcopy(temp_list)
                    if len(temp_list_copy) > 0:
                        pre_group = temp_list_copy.pop(-1)
                        pre_group.append(int(s[i]))
                        pre_str = ''.join(list(map(lambda x: str(x), pre_group)))
                        pre_nums = int(pre_str)
                        if pre_nums <= 255 and str(pre_nums)==pre_str:
                            temp_list_copy.append(pre_group)
                            back_track(i + 1, temp_list_copy)

        back_track(0, [])
        new_result = []
        for result in result_list:
            result_str = ''
            for group in result:
                group =''.join(list(map(lambda x: str(x), group)))
                result_str+=group+'.'
            new_result.append(result_str[:-1])
        return new_result


s = Solution()
print(s.restoreIpAddresses("010010"))
