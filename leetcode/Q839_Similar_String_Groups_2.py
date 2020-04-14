from typing import List


class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        set_list=[]
        for i in range(len(A)):
            a = A[i]
            inner_set_list =[]
            k=0
            while k <len(set_list):
                k_set=set_list[k]
                if i in k_set:
                    inner_set_list.append(set_list.pop(k))
                else:
                    k+=1
            if len(inner_set_list)>0:
                a_set=inner_set_list[0]
                for k in range(1,len(inner_set_list)):
                    a_set=a_set.union(inner_set_list[k])
            else:
                a_set = set()
                a_set.add(i)
            for j in range(i+1,len(A)):
                b = A[j]
                flag = [1] * len(b)
                is_sim = False
                for k in range(len(b)):
                    if a[k] != b[k]:
                        flag[k] = 0
                if len(b) - sum(flag) == 2:
                    pre_k = -1
                    for k in range(len(flag)):
                        if flag[k] == 0:
                            if pre_k == -1:
                                pre_k = k
                            else:
                                if a[pre_k] == b[k] and b[pre_k] == a[k]:
                                    is_sim = True
                elif len(b) - sum(flag) == 0:
                    is_sim = True
                if is_sim:
                    a_set.add(j)
            set_list.append(a_set)
        return len(set_list)
s =Solution()
# print(s.numSimilarGroups(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]))
print(s.numSimilarGroups(["tars","rats","arts","star"]))



