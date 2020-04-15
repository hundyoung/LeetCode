from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        result =[]
        def back_track(s:str,temp:list):
            if s=='':
                result.append(temp)
            else:
                for i in range(len(s)):
                    back_track(s[:i]+s[i+1:],temp+s[i])
        back_track(S,'')
        return result
s = Solution()
print(s.permutation("qwe"))

