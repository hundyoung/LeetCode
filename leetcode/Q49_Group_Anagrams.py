from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a={'a':2,'b':3,'c':4}
        # b={'a':2,'c':4,'b':3}
        # c={a:a}
        # print(b in c)
        # return ["asd"]
        str_dict={}
        for word in (strs):
            new_str = ''.join(sorted(word))
            if new_str not in str_dict:
                str_dict[new_str]  = []
            str_dict[new_str].append(word)
        return list(str_dict.values())

s=Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))