from typing import List

import copy
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        # result = False
        # # temp_lilst =[]
        # operation = ['+','-','*','/']
        result_set = set()
        def back_track(to_process:list):
            if len(to_process)==1:
                if -0.01<to_process[0]-24<0.01:
                    result_set.add(True)
            else:
                for i in range(len(to_process)):
                    n_1 = to_process[i]
                    for j in range(len(to_process)):
                        if j != i:
                            n_2 = to_process[j]

                            to_process_copy = copy.deepcopy(to_process)
                            to_process_copy.remove(n_1)
                            to_process_copy.remove(n_2)

                            to_process_copy_2 = copy.deepcopy(to_process_copy)
                            r = n_1+n_2
                            to_process_copy_2.append(r)
                            back_track(to_process_copy_2)

                            to_process_copy_2 = copy.deepcopy(to_process_copy)
                            r = n_1*n_2
                            to_process_copy_2.append(r)
                            back_track(to_process_copy_2)

                            to_process_copy_2 = copy.deepcopy(to_process_copy)
                            r = n_1-n_2
                            to_process_copy_2.append(r)
                            back_track(to_process_copy_2)

                            to_process_copy_2 = copy.deepcopy(to_process_copy)
                            if n_2!=0:
                                r= n_1/n_2
                                to_process_copy_2.append(r)
                                back_track(to_process_copy_2)
        back_track(nums)
        return len(result_set)>0

s= Solution()
print(s.judgePoint24([1,1,7,7]))
