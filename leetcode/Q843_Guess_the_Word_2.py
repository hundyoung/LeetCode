# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def __init__(self,word:str,count):
        self.target = word
        self.count = count
    def guess(self, word: str) -> int:
        distance = 0
        word_a=self.target
        for k in range(len(word_a)):
            if word_a[k] == word[k]:
                distance += 1
        self.count-=1
        if distance==6:
            print('Y',self.count)
        if self.count==0:
            print('N')
        return distance
from typing import List


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        word_dist_dict = {}
        flag_dict = {}
        max_dist_word = ''
        max_dict = 0
        for i in range(len(wordlist)):
            word_a = wordlist[i]
            dist_dict = word_dist_dict.get(word_a, {})
            flag_dict[word_a]= True
            for j in range(0,len(wordlist)):
                if i!=j:
                    word_b = wordlist[j]
                    distance = 0

                    for k in range(len(word_a)):
                        if word_a[k]==word_b[k]:
                            distance+=1
                    if distance>max_dict:
                        max_dist_word=word_b
                        max_dict=distance
                    dist_dict[word_b] = distance
            word_dist_dict[word_a]=dist_dict
        c = master.guess(max_dist_word)
        if c == 6:
            return
        else:
            flag_dict[max_dist_word] = False
            for j in range(0, len(wordlist)):
                next_word = wordlist[j]
                if flag_dict[next_word] and word_dist_dict[max_dist_word][next_word] != c:
                    flag_dict[next_word] = False
        for i in range(len(wordlist)):
            word = wordlist[i]
            if flag_dict[word]:
                c = master.guess(word)
                if c ==6:
                    return
                else:
                    flag_dict[word]=False
                    for j in range(i+1,len(wordlist)):
                        next_word = wordlist[j]
                        if flag_dict[next_word] and word_dist_dict[word][next_word]!=c:
                            flag_dict[next_word] = False

s= Solution()

target,wordlist,count = "ccoyyo",["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"],10
print(s.findSecretWord(wordlist,Master(target,count)))

