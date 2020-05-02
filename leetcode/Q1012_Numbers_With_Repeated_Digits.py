class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        number_str = str(N)
        count =0
        flag =True
        n_set=set()
        for i in range(len(number_str)):
            if number_str[i] not in n_set:
                n_set.add(number_str[i])
            else:
                flag=False
        if flag:
            count+=1
        for i in range(len(number_str)-1):
            current_count =9
            for j in range(9,9-i,-1):
                current_count*=j
            count+=current_count

        current_count = int(number_str[0])-1
        for i in range(9,9-len(number_str)+1,-1):
            current_count*=i
        count+=current_count
        for i in range(1,len(number_str)):
            n = int(number_str[i])
            current_count=n
            for j in range(len(number_str)-i-1):
                t=(9-i-1)-j
                current_count*=t
            count+=current_count
        return N-count
s = Solution()
print(s.numDupDigitsAtMostN(12))


