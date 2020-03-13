from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(list(map(lambda x:str(x),digits))))
        num+=1
        return list(map(lambda x:int(x),list(str(num))))


s = Solution()
print(s.plusOne([9,9]))