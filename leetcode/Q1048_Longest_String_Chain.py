from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp=[1]*len(words)
        words=sorted(words,key=lambda x:len(x))
        for i in range(len(words)):
            word=words[i]
            word_len=len(word)
            for j in range(i-1,-1,-1):
                pre_word=words[j]
                if len(pre_word)==word_len:
                    continue
                elif len(pre_word)<word_len-1:
                    break
                for k in range(len(word)):
                    new_word= word[:k]+word[k+1:]
                    if new_word==pre_word:
                        dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
s = Solution()
print(s.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))
