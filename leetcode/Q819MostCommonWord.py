from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bannedDict = {}
        for i in range(len(banned)):
            bannedDict[banned[i]] = banned[i]

        # words = paragraph.replace("!"," ")
        # words = paragraph.replace("?"," ")
        # words = paragraph.replace("'"," ")
        # words = paragraph.replace(","," ")
        # words = paragraph.replace(";"," ")
        # words = paragraph.replace("."," ")
        wordDict = {}
        maxWordCount = 0
        maxWord = ""
        i = 0
        while i <len(paragraph):
            if paragraph[i].isalpha():
                j = i+1
                while j<len(paragraph) and paragraph[j].isalpha():
                    j = j+1
                word = paragraph[i:j].lower()
                if word not in bannedDict:
                    if word in wordDict:
                        wordDict[word] = wordDict[word]+1
                    else:
                        wordDict[word] = 1
                    if maxWordCount<wordDict[word]:
                        maxWordCount=wordDict[word]
                        maxWord = word
                i = j+1
            else:
                i = i+1
        return maxWord


paragraph = "Bob"
banned = []

s = Solution()
print(s.mostCommonWord(paragraph,banned))


