from typing import List


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        is_bold = [False]*len(S)
        for word in words:
            for i in range(len(S)-len(word)+1):
                s = S[i:i+len(word)]
                if s == word:
                    for j in range(i,i+len(word)):
                        is_bold[j]=True
        i=0
        result =''
        while i <len(is_bold):
            if is_bold[i]:
                result+='<b>'+S[i]
                j=i+1
                while j<len(S) and is_bold[j]:
                    result +=S[j]
                    j+=1
                result += '</b>'+S[j] if j<len(S) else '</b>'
                i=j+1
            else:
                result += S[i]
                i+=1
        return result
s =Solution()
words =["ccb","b","d","cba","dc"]
S = "eeaadadadc"
print(s.boldWords(words,S))


