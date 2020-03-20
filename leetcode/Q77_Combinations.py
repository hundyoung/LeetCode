from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result_list = []
        def back_track(i,temp:List[int]):
            if len(temp)==k:
                result_list.append(temp)
                return
            else:
                if i<=n:

                    temp_copy =list(temp)
                    temp_copy.append(i)
                    back_track(i+1,temp)

                    back_track(i+1,temp_copy)

        back_track(1,[])
        return result_list
s = Solution()
print(s.combine(4,2))