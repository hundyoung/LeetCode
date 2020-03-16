from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        result_set = set(words)
        for word in words_set:
            for i in range(1,len(word)):
                sub_word = word[i:]
                if sub_word in words_set:
                    if sub_word in result_set:
                        result_set.remove(sub_word)
        return len(result_set)+len(''.join(result_set))

s = Solution()
words = ["time", "atime", "btime"]
print(s.minimumLengthEncoding(words))