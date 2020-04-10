class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_dict={}
        for i in range(len(keyboard)):
            key_dict[keyboard[i]]=i
        count = key_dict[word[0]]
        pre_i = key_dict[word[0]]
        for j in range(1,len(word)):
            i = key_dict[word[j]]
            count+=(max(i,pre_i)-min(i,pre_i))
            pre_i = i
        return count
s =Solution()
keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
print(s.calculateTime(keyboard,word))