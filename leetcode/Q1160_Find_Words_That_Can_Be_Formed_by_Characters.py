from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict={}
        result=0
        for c in chars:
            char_dict[c]= char_dict.get(c,0)+1
        for word in words:
            is_enough=True
            char_dict_copy = char_dict.copy()
            for c in word:
                existing_n=char_dict_copy.get(c,0)
                if existing_n>=1:
                    char_dict_copy[c]=existing_n-1
                else:
                    is_enough=False
                    break
            if is_enough:
                result+=len(word)
        return result
s = Solution()
print(s.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
