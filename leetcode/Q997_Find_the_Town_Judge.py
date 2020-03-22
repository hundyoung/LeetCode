from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and N==1:
            return 1
        elif len(trust)==0:
            return -1
        trust_dict ={}
        be_trusted_dict = {}
        result = []
        for t_p,b_t_p in trust:
            trust_dict[t_p] = trust_dict.get(t_p,[])+[b_t_p]
            be_trusted_dict[b_t_p]= be_trusted_dict.get(b_t_p,[])+[t_p]
        for person in be_trusted_dict:
            if len(be_trusted_dict[person])==N-1 and person not in trust_dict:
                result.append(person)
                if len(result)>1:
                    return -1
        if len(result)==1:
            return result[0]
        else:
            return -1
s= Solution()
print(s.findJudge(N = 2, trust = [[1,2]]))
