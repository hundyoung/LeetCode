# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def __init__(self,word:str):
        self.target = word
    def guess(self, word: str) -> int:
        distance = 0
        word_a=self.target
        for k in range(len(word_a)):
            if word_a[k] == word[k]:
                distance += 1
        return distance
from typing import List


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        # position_list = []
        # for i in range(6):
        #     position_list.append({})
        # for i in range(len(wordlist)):
        #     word = wordlist[i]
        #     for j in range(len(word)):
        #         char = word[j]
        #         p_d = position_list[j]
        #         char_set = p_d.get(char,set())
        #         char_set.add(word)
        #         p_d[char]=char_set
        #         position_list[j]=p_d
        word_dist_dict = {}
        max_dist=0
        max_dist_word1=''
        max_dist_word2=''
        for i in range(len(wordlist)):
            word_a = wordlist[i]
            dist_dict = word_dist_dict.get(word_a, {})
            for j in range(0,len(wordlist)):
                if i!=j:
                    word_b = wordlist[j]
                    distance = 0
                    for k in range(len(word_a)):
                        if word_a[k]!=word_b[k]:
                            distance+=1
                    if distance>max_dist:
                        max_dist=distance
                        max_dist_word1=word_a
                        max_dist_word2=word_b
                    dist_dict[word_b] = distance
            word_dist_dict[word_a]=dist_dict

        dist_list = []
        dist_list.append((max_dist_word1,0))
        dist_list+=list(sorted(word_dist_dict[max_dist_word1].items(),key=lambda x:x[1]))
        left = 0
        right = len(dist_list)-1
        while left<=right:
            if right>=len(dist_list) or left>=len(dist_list):
                break
            if left<0 or right<0:
                break
            mid = (left+right)>>1
            c_mid = master.guess(dist_list[mid][0])
            if c_mid==6:
                print("Yes")

                return
            else:
                c1 = master.guess(dist_list[left][0])
                if c1 == 6:
                    print("Yes")

                    return
                c2 = master.guess(dist_list[right][0])
                if c2 == 6:
                    print("Yes")

                    return
                if c_mid-c1<=c_mid-c2:
                    right=mid-1
                else:
                    left=mid
s= Solution()

target = "hbaczn"
wordlist = ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]

print(s.findSecretWord(wordlist,Master(target)))

