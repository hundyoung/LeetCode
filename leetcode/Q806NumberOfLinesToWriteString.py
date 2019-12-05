from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        totalLen = 0
        lineCount =1
        aIndex = ord('a')
        for i in range(len(S)):
            currentLenth=widths[ord(S[i])-aIndex]
            if totalLen+currentLenth>100:
                lineCount+=1
                totalLen=currentLenth
            else:
                totalLen+=currentLenth
        return [lineCount,totalLen]


s = Solution()
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
AAAA = "bbbcccdddaaa"
print(s.numberOfLines(widths,AAAA))
