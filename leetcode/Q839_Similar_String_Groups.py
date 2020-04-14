from typing import List


class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        group_dict={}
        for i in range(len(A)):
            a = A[i]
            b_set=group_dict.get(a,[])
            for j in range(i+1,len(A)):
                b = A[j]
                flag = [1]*len(b)
                is_sim=False
                for k in range(len(b)):
                    if a[k]!=b[k]:
                        flag[k]=0
                if len(b)-sum(flag)==2:
                    pre_k=-1
                    for k in range(len(flag)):
                        if flag[k]==0:
                            if pre_k==-1:
                                pre_k=k
                            else:
                                if a[pre_k]==b[k] and b[pre_k]==a[k]:
                                    is_sim=True
                elif len(b)-sum(flag)==0:
                    is_sim = True
                if is_sim:
                    b_set.append(b)
                    c_set = group_dict.get(b, [])
                    c_set.append(a)
                    group_dict[b]=c_set
            group_dict[a] = b_set
        for a in group_dict:
            b_set = group_dict[a]
            if b_set==-1:
                continue
            done = set()
            done.add(a)
            while len(b_set)>0:
                b = b_set.pop(0)
                if b in group_dict and group_dict[b]!=-1:
                    for i in range(len(group_dict[b])):
                        c = group_dict[b][i]
                        if c not in b_set and c not in done:
                            b_set.append(c)
                    group_dict[b]=-1
                done.add(b)
            group_dict[a]=done
        count =0
        for a in group_dict:
            if group_dict[a]!=-1:
                count+=1
        return count
s =Solution()
print(s.numSimilarGroups(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]))
# print(s.numSimilarGroups(["tars","rats","arts","star"]))



